def hitung_total(pilihan_barang):
    harga_barang = {
        "Tomat": 5000,
        "Timun": 4000,
        "Telur": 2000,
        "Tepung": 6000
    }

    belanja = pilihan_barang
    diskon = belanja * (10/100)
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

    for b in barang:
        print(b)

    pilihan_barang = input("\nMasukan barang yg mau dibeli: ")

    if pilihan_barang in barang:
        print("Barang diterima!")
        total_bayar = hitung_total(pilihan_barang)
        print(f"Total yg harus dibayar adalah: {total_barang}")

    else:
        print("Barang tidak ada!")

while True:
    print("\n=== KASIR SEDERHANA ===")
    print("\n1.Belanja")
    print("2.Lihat riwayat belanjaan")
    print("3.Hapus daftar belanjaan")
    print("4.Keluar")

    pilihan = int(input("\nMasukan pilihan (1-4): "))

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


