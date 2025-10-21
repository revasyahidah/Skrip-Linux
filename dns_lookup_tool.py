import subprocess
import re

def run_nslookup(domain):
    print(f"Menjalankan nslookup untuk domain: {domain}\n")

    try:
        # Jalankan perintah nslookup
        result = subprocess.run(["nslookup", domain], capture_output=True, text=True)
        output = result.stdout

        # Tampilkan hasil lengkap
        print(output)

        # Analisis hasil
        analyze_nslookup(output)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

def analyze_nslookup(output):
    # Cari alamat IP menggunakan regex
    ip_match = re.findall(r"Address:\s+([\d\.]+)", output)

    print("\n=== Hasil Analisis DNS ===")
    if ip_match:
        for i, ip in enumerate(ip_match):
            print(f"Alamat IP [{i+1}]: {ip}")
        print("✅ Domain berhasil diresolusi oleh DNS.")
    else:
        print("❌ Domain tidak ditemukan atau DNS tidak dapat melakukan resolusi nama.")

# Jalankan nslookup pada domain tertentu
domain = "www.google.com"
run_nslookup(domain)
