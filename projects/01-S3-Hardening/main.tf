resource "aws_s3_bucket" "secure_bucket" {
  bucket = "frankfru-secure-data-2026"
}

# 1. Block all public access (Stops data leaks)
resource "aws_s3_bucket_public_access_block" "public_access" {
  bucket                  = aws_s3_bucket.secure_bucket.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# 2. Force Encryption (Protects data at rest)
resource "aws_s3_bucket_server_side_encryption_configuration" "encryption" {
  bucket = aws_s3_bucket.secure_bucket.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# 3. Enable Versioning (Protects against accidental deletion)
resource "aws_s3_bucket_versioning" "versioning" {
  bucket = aws_s3_bucket.secure_bucket.id
  versioning_configuration {
    status = "Enabled"
  }
}

# 4. Access Logging (Resolves CKV_AWS_18)
# Requires a separate bucket to store the logs
resource "aws_s3_bucket" "log_bucket" {
  bucket = "frankfru-logs-2026"
}

resource "aws_s3_bucket_logging" "secure_logging" {
  bucket = aws_s3_bucket.secure_bucket.id

  target_bucket = aws_s3_bucket.log_bucket.id
  target_prefix = "log/"
}

# 5. Cross-Region Replication (Resolves CKV_AWS_144)
# Note: This is a high-level example. In a real environment, 
# you would define a destination bucket in a different region.
resource "aws_s3_bucket_replication_configuration" "replication" {
  # Must enable versioning on both buckets for replication to work
  depends_on = [aws_s3_bucket_versioning.versioning]

  role   = aws_iam_role.replication_role.arn
  bucket = aws_s3_bucket.secure_bucket.id

  rules {
    id     = "replicate-all"
    status = "Enabled"

    destination {
      bucket        = aws_s3_bucket.destination.arn
      storage_class = "STANDARD"
    }
  }
}

# IAM Role required for replication
resource "aws_iam_role" "replication_role" {
  name = "s3-replication-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "s3.amazonaws.com"
        }
      },
    ]
  })
}
