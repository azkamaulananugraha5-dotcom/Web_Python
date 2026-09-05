# 1. Ubah nama fungsi agar tidak bentrok dengan fungsi bawaan Python
def hitung_total(pilihan_barang):
    # Contoh simulasi harga barang (karena di kode Anda belum ada harga)
    harga_barang = {
        "Tomat": 5000,
        "Timun": 4000,
        "Telur": 3000,
        "Tepung": 6000
    }
    
    # Mengambil harga berdasarkan input, jika tidak ada default ke 0
    belanja = harga_barang.get(pilihan_barang, 0)
    diskon = belanja * (10 / 100) # Perbaikan formula diskon 10%
    total = belanja - diskon
    return total

def belanjaan():
    print("\nPilih Barang yg ada di bawah ini: ")
    
    barang = [
        "Tomat",
        "Timun",
        "Telur",
        "Tepung"
    ]
    
    # Menggunakan perulangan (loop) agar lebih rapi
    for b in barang:
        print(b)
        
    pilihan_barang = input("\nMasukan barang yg mau dibeli: ")
    
    # Perbaikan logika pengecekan barang menggunakan operator 'in'
    if pilihan_barang in barang:
        print("Barang diterima!")
        # Memanggil fungsi hitung_total dan menampilkan hasilnya
        total_bayar = hitung_total(pilihan_barang)
        print(f"Total yang harus dibayar setelah diskon: Rp{total_bayar:.0f}")
    else:
        print("Barang tidak ada!")

# Menu Utama
while True:
    print("\n=== DAFTAR ===")
    print("1. Belanja")
    print("2. Lihat riwayat belanjaan")
    print("3. Hapus daftar belanjaan!")
    print("4. Keluar")
    
    try:
        pilihan = int(input("\nMasukan pilihan (1-4): "))
    except ValueError:
        print("Input harus berupa angka!")
        continue
        
    if pilihan == 1:
        belanjaan()
    elif pilihan == 2:
        print("Daftar belanjaan")
    elif pilihan == 3:
        print("Daftar belanjaan dihapus!")
    elif pilihan == 4:
        break
    else:
        print("Input tidak valid!")
