import boto3
import time

def auto_remediate(bucket_name):
    """
    Automated Response: Deletes the bucket to prevent further unauthorized access.
    """
    # Note: We use the localstack endpoint here
    s3 = boto3.client('s3', endpoint_url='http://localhost:4566', region_name='us-east-1')
    print(f"🛠️  INTRUSION RESPONSE INITIATED: Securing environment...")
    
    try:
        s3.delete_bucket(Bucket=bucket_name)
        print(f"✅ SUCCESS: Bucket '{bucket_name}' has been deleted to stop the attack.")
    except Exception as e:
        print(f"❌ Remediation failed: {e}")

def monitor_live_cloud_traffic():
    s3 = boto3.client('s3', endpoint_url='http://localhost:4566', region_name='us-east-1')
    bucket_to_watch = "cloud-security-logs-bucket"

    print("🚨 Live Cloud Detection Engine Active...")
    
    request_count = 0
    start_time = time.time()

    while request_count < 10:
        try:
            s3.list_buckets()
            request_count += 1
            elapsed = time.time() - start_time
            print(f"📥 Request {request_count} detected at {elapsed:.2f}s")

            # DETECTION LOGIC
            if request_count > 5 and elapsed < 3:
                print("🛑 CRITICAL ALERT: Rapid API activity detected!")
                
                # --- CALL THE REMEDIATION HERE ---
                auto_remediate(bucket_to_watch)
                # ---------------------------------
                
                break
                
            time.sleep(0.3)
        except Exception as e:
            print(f"Monitor stopped: {e}")
            break

if __name__ == "__main__":
    monitor_live_cloud_traffic()