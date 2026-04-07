import os

# Example attacker IP (replace dynamically if needed)
ip = "192.168.1.100"

# Block IP using firewall
os.system(f"iptables -A INPUT -s {ip} -j DROP")

print(f"Blocked malicious IP: {ip}")
