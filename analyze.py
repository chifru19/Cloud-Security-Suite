import matplotlib
matplotlib.use('Agg') # Essential for macOS backend saving
import matplotlib.pyplot as plt
from scapy.all import rdpcap, IP, TCP, UDP, ICMP, Raw
import os
from collections import Counter

# 1. DYNAMIC FILE DISCOVERY
target_file = next((f for f in os.listdir('.') if f.startswith('my_traffic')), None)

if not target_file:
    print("Error: No capture file found starting with 'my_traffic'.")
else:
    print(f"--- STARTING ULTIMATE ANALYSIS: {target_file} ---")
    pkts = rdpcap(target_file)
    
    # Data Storage
    ips, protocols, latencies = [], [], []
    ping_matches = {}
    pass_alerts = []
    keywords = [b"user", b"pass", b"login", b"pwd", b"auth", b"email"]

    # 2. THE PROCESSING ENGINE (Single-Pass Analysis)
    for i, p in enumerate(pkts):
        if p.haslayer(IP):
            src_ip = p[IP].src
            ips.append(src_ip)
            
            # Protocol & Latency Calculation
            if p.haslayer(TCP): protocols.append('TCP (Web/Apps)')
            elif p.haslayer(UDP): protocols.append('UDP (Streaming/DNS)')
            elif p.haslayer(ICMP): 
                protocols.append('ICMP (Ping)')
                if p[ICMP].type == 8: ping_matches[(p[ICMP].id, p[ICMP].seq)] = p.time
                elif p[ICMP].type == 0:
                    key = (p[ICMP].id, p[ICMP].seq)
                    if key in ping_matches:
                        latencies.append((p.time - ping_matches[key]) * 1000)
            else: protocols.append('Other')

            # THE SECURITY SNIFFER (Password Tracking)
            if p.haslayer(Raw):
                payload = p[Raw].load.lower()
                for word in keywords:
                    if word in payload:
                        pass_alerts.append({
                            "packet": i, "src": src_ip, "dst": p[IP].dst,
                            "term": word.decode(), "snippet": payload[:50]
                        })

    # 3. CONSOLE REPORT
    print(f"\n[+] Total Packets Analyzed: {len(pkts)}")
    if latencies: print(f"[+] Average Latency: {sum(latencies)/len(latencies):.2f} ms")
    
    print(f"\n[!] SECURITY AUDIT [!]")
    if pass_alerts:
        print(f"FOUND {len(pass_alerts)} POTENTIAL CLEARTEXT LEAKS:")
        for alert in pass_alerts[:5]:
            print(f" - Pkt #{alert['packet']} ({alert['src']} -> {alert['dst']}): "
                  f"Keyword '{alert['term']}' found in: {alert['snippet']}...")
    else: print("No cleartext passwords found. Traffic appears secure.")

    # 4. DATA VISUALIZATION
    plt.figure(figsize=(10, 6))
    top_10 = Counter(ips).most_common(10)
    plt.bar([x[0] for x in top_10], [x[1] for x in top_10], color='skyblue', edgecolor='navy')
    plt.title(f'Top 10 Traffic Sources\n({target_file})'); plt.xticks(rotation=45); plt.tight_layout()
    plt.savefig('top_talkers.png')

    plt.figure(figsize=(8, 8))
    proto_counts = Counter(protocols)
    plt.pie(proto_counts.values(), labels=proto_counts.keys(), autopct='%1.1f%%', startangle=140)
    plt.title('Network Protocol Distribution'); plt.savefig('protocol_distribution.png')

    print("\n--- ANALYSIS COMPLETE ---")
    print("Files ready for portfolio: 'top_talkers.png' and 'protocol_distribution.png'")
