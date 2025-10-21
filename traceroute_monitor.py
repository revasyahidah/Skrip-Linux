import os
import platform
import subprocess

def run_traceroute(host):
    # Menyesuaikan perintah traceroute sesuai OS
    if platform.system().lower() == "windows":
        cmd = ["tracert", host]
    else:
        cmd = ["traceroute", host]
    
    print(f"\n=== Traceroute ke {host} ===")
    try:
        # Menjalankan traceroute dan menangkap output
        result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Terjadi kesalahan saat menjalankan traceroute: {e}")

# Daftar host tujuan traceroute
hosts = ["8.8.8.8", "1.1.1.1", "www.cisco.com"]

print("=== Program Traceroute Otomatis ===")
for host in hosts:
    run_traceroute(host)
print("\nSelesai melakukan traceroute ke semua host.")
