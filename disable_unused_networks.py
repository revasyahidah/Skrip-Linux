#!/usr/bin/env python3

import subprocess
import time
import os

POLL_INTERVAL = 5  # detik antar pengecekan ulang

def run(cmd):
    """Jalankan perintah shell dan ambil hasilnya"""
    return subprocess.run(cmd, shell=True, capture_output=True, text=True).stdout.strip()

def get_default_interface():
    """Ambil interface default (yang punya default gateway)"""
    output = run("ip route show default")
    for line in output.splitlines():
        parts = line.split()
        if "dev" in parts:
            idx = parts.index("dev")
            return parts[idx + 1]
    return None

def list_all_interfaces():
    """Daftar semua interface fisik (skip loopback)"""
    output = run("ls /sys/class/net")
    return [iface for iface in output.split() if iface != "lo"]

def get_operstate(iface):
    """Cek apakah interface dalam keadaan 'up' atau 'down'"""
    try:
        with open(f"/sys/class/net/{iface}/operstate") as f:
            return f.read().strip()
    except:
        return "unknown"

def has_ip_address(iface):
    """Cek apakah interface punya IP address"""
    output = run(f"ip addr show {iface}")
    return "inet " in output

def disable_interface(iface):
    """Nonaktifkan interface menggunakan ip"""
    print(f"[!] Menonaktifkan interface: {iface}")
    run(f"ip link set dev {iface} down")

def main():
    if os.geteuid() != 0:
        print("❌ Jalankan skrip ini sebagai root (gunakan sudo)")
        return

    default_iface = get_default_interface()
    print(f"🔌 Interface utama (default route): {default_iface}")

    if default_iface is None:
        print("❌ Tidak ditemukan default route. Keluar.")
        return

    interfaces = list_all_interfaces()

    for iface in interfaces:
        if iface == default_iface:
            print(f"[OK] {iface} adalah interface utama — tidak dinonaktifkan.")
            continue

        state = get_operstate(iface)
        has_ip = has_ip_address(iface)
        print(f"⏺️ {iface}: state={state}, IP={has_ip}")

        if state == "down":
            print(f"  └── Interface {iface} sudah down, menonaktifkan untuk memastikan.")
            disable_interface(iface)
        elif not has_ip:
            print(f"  └── Interface {iface} tidak punya IP — menonaktifkan.")
            disable_interface(iface)
        else:
            print(f"  └── Interface {iface} aktif tapi bukan default — menonaktifkan.")
            disable_interface(iface)

    print("✅ Semua interface non-utama telah diperiksa.")

    # Monitoring loop: pantau interface yang tiba-tiba down
    print(f"📡 Memantau setiap {POLL_INTERVAL} detik... Tekan Ctrl+C untuk keluar.")
    try:
        while True:
            for iface in list_all_interfaces():
                if iface == default_iface:
                    continue
                state = get_operstate(iface)
                if state == "down":
                    disable_interface(iface)
            time.sleep(POLL_INTERVAL)
    except KeyboardInterrupt:
        print("\n👋 Dihentikan oleh pengguna. Keluar.")

if __name__ == "__main__":
    main()
