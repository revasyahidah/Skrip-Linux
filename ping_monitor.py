import os
import platform
import time

# Fungsi untuk melakukan ping ke satu host
def ping_host(host):
    # Menentukan parameter ping berdasarkan OS (Windows/Linux)
    param = "-n 1" if platform.system().lower() == "windows" else "-c 1"
    # Menjalankan perintah ping
    response = os.system(f"ping {param} {host} > /dev/null 2>&1")
    # Mengevaluasi hasil ping
    if response == 0:
        return True
    else:
        return False

# Daftar host yang akan dicek
hosts = ["8.8.8.8", "1.1.1.1", "192.168.1.1", "10.0.0.1"]

print("=== Monitoring Konektivitas Jaringan ===")
print("Tekan Ctrl + C untuk menghentikan program.\n")

try:
    while True:
        for host in hosts:
            status = ping_host(host)
            if status:
                print(f"{host} ✅ UP (terhubung)")
            else:
                print(f"{host} ❌ DOWN (tidak terhubung)")
        print("-" * 50)
        time.sleep(5)  # jeda 5 detik sebelum ping ulang
except KeyboardInterrupt:
    print("\nMonitoring dihentikan oleh pengguna.")
