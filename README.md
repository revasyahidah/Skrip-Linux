# Script-Linux
Skrip python yang digunakan untuk pembelajaran Otomatisasi Jaringan

Hasil Eksekusi Program
1. disable_unused_networks.py
devasc@labvm:~$ chmod +x disable_unused_networks.py
devasc@labvm:~$ sudo ./disable_unused_networks.py
🔌 Interface utama (default route): enp0s3
⏺️ dummy0: state=down, IP=True
  └── Interface dummy0 sudah down, menonaktifkan untuk memastikan.
[!] Menonaktifkan interface: dummy0
[OK] enp0s3 adalah interface utama — tidak dinonaktifkan.
✅ Semua interface non-utama telah diperiksa.
📡 Memantau setiap 5 detik... Tekan Ctrl+C untuk keluar.
[!] Menonaktifkan interface: dummy0
[!] Menonaktifkan interface: dummy0
^C
👋 Dihentikan oleh pengguna. Keluar.

2. ping_monitor.py
devasc@labvm:~$ python3 ping_monitor.py
=== Monitoring Konektivitas Jaringan ===
Tekan Ctrl + C untuk menghentikan program.

8.8.8.8 ✅ UP (terhubung)
1.1.1.1 ✅ UP (terhubung)
192.168.1.1 ❌ DOWN (tidak terhubung)
10.0.0.1 ❌ DOWN (tidak terhubung)

3. traceroute_monitor.py
devasc@labvm:~$ python3 traceroute_monitor.py
=== Program Traceroute Otomatis ===

=== Traceroute ke 8.8.8.8 ===
traceroute to 8.8.8.8 (8.8.8.8), 64 hops max
  1   10.0.2.2  0.401ms  0.267ms  0.244ms 
  2   10.0.2.2  0.733ms  0.684ms  0.574ms 


=== Traceroute ke 1.1.1.1 ===
traceroute to 1.1.1.1 (1.1.1.1), 64 hops max
  1   10.0.2.2  0.339ms  0.231ms  0.295ms 
  2   10.0.2.2  0.879ms  0.586ms  0.501ms 


=== Traceroute ke www.cisco.com ===
traceroute to e2867.dsca.akamaiedge.net (23.36.49.21), 64 hops max
  1   10.0.2.2  0.305ms  0.262ms  0.152ms 
  2   10.0.2.2  0.614ms  0.676ms  0.724ms 


Selesai melakukan traceroute ke semua host.

4. dns_lookup_tool.py
devasc@labvm:~$ python3 dns_lookup_tool.py
Menjalankan nslookup untuk domain: www.google.com

Server:        127.0.0.53
Address:    127.0.0.53#53

Non-authoritative answer:
Name:    www.google.com
Address: 74.125.130.106
Name:    www.google.com
Address: 74.125.130.105
Name:    www.google.com
Address: 74.125.130.99
Name:    www.google.com
Address: 74.125.130.104
Name:    www.google.com
Address: 74.125.130.103
Name:    www.google.com
Address: 74.125.130.147
Name:    www.google.com
Address: 2404:6800:4003:c11::6a
Name:    www.google.com
Address: 2404:6800:4003:c11::93
Name:    www.google.com
Address: 2404:6800:4003:c11::68
Name:    www.google.com
Address: 2404:6800:4003:c11::67



=== Hasil Analisis DNS ===
Alamat IP [1]: 127.0.0.53
Alamat IP [2]: 74.125.130.106
Alamat IP [3]: 74.125.130.105
Alamat IP [4]: 74.125.130.99
Alamat IP [5]: 74.125.130.104
Alamat IP [6]: 74.125.130.103
Alamat IP [7]: 74.125.130.147
Alamat IP [8]: 2404
Alamat IP [9]: 2404
Alamat IP [10]: 2404
Alamat IP [11]: 2404
✅ Domain berhasil diresolusi oleh DNS.
