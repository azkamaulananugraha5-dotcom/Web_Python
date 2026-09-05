import pandas as pd
import numpy as np
import os
from datetime import datetime

# ============================================================
# PENGATURAN
# ============================================================
FILE_RIWAYAT = "riwayat_balap.csv"
FILE_STATISTIK = "statistik_100.csv"

KARAKTER = [
    "Master Penghancur",
    "Prajurit Tekken",
    "Penjelajah Laut",
    "Angin Puting Beliung",
    "Ksatria yang Berlari Kencang",
    "Raja"
]

# Statistik default (dari 100 race terakhir yang kamu kirim)
DEFAULT_WINS = {
    "Master Penghancur": 16,
    "Prajurit Tekken": 24,
    "Penjelajah Laut": 17,
    "Angin Puting Beliung": 20,
    "Ksatria yang Berlari Kencang": 8,
    "Raja": 15
}

# ============================================================
# FUNGSI BANTUAN
# ============================================================
def load_riwayat():
    if os.path.exists(FILE_RIWAYAT):
        df = pd.read_csv(FILE_RIWAYAT)
        return df
    else:
        # Data awal dari 10 race yang kamu kirim
        data_awal = [
            [3, 1, 5, 6, 4, 2],
            [6, 5, 1, 4, 2, 3],
            [5, 3, 1, 6, 4, 2],
            [3, 5, 1, 6, 4, 2],
            [5, 1, 3, 4, 2, 6],
            [2, 3, 1, 4, 5, 6],
            [1, 6, 3, 4, 5, 2],
            [4, 2, 5, 6, 3, 1],
            [3, 1, 6, 5, 2, 4],
            [3, 6, 5, 2, 1, 4],
        ]
        df = pd.DataFrame(data_awal, columns=KARAKTER)
        df["Waktu"] = datetime.now().strftime("%Y-%m-%d %H:%M")
        df.to_csv(FILE_RIWAYAT, index=False)
        return df

def load_statistik():
    if os.path.exists(FILE_STATISTIK):
        df = pd.read_csv(FILE_STATISTIK)
        return dict(zip(df["Karakter"], df["Menang"]))
    else:
        df = pd.DataFrame({
            "Karakter": list(DEFAULT_WINS.keys()),
            "Menang": list(DEFAULT_WINS.values())
        })
        df.to_csv(FILE_STATISTIK, index=False)
        return DEFAULT_WINS.copy()

def simpan_statistik(wins):
    df = pd.DataFrame({
        "Karakter": list(wins.keys()),
        "Menang": list(wins.values())
    })
    df.to_csv(FILE_STATISTIK, index=False)

def tampilkan_analisis(df, wins):
    print("\n" + "="*60)
    print("ANALISIS DATA BALAP")
    print("="*60)

    total = sum(wins.values())
    print("\n1. WIN RATE (berdasarkan statistik 100 race)")
    for k, v in sorted(wins.items(), key=lambda x: x[1], reverse=True):
        print(f"   {k:32s} : {v:2d} menang ({v/total*100:.1f}%)")

    if len(df) == 0:
        print("\nBelum ada data riwayat.")
        return

    print(f"\n2. RIWAYAT TERAKHIR ({len(df)} race)")
    print(df[KARAKTER].tail(10).to_string())

    print("\n3. RATA-RATA POSISI (10 race terakhir)")
    avg = df[KARAKTER].tail(10).mean().sort_values()
    for k, v in avg.items():
        print(f"   {k:32s} : {v:.2f}")

    print("\n4. JUMLAH JUARA (posisi 1) di 10 race terakhir")
    juara = (df[KARAKTER].tail(10) == 1).sum().sort_values(ascending=False)
    for k, v in juara.items():
        print(f"   {k:32s} : {v} kali")

    print("\n5. MASUK TOP 3 di 10 race terakhir")
    top3 = (df[KARAKTER].tail(10) <= 3).sum().sort_values(ascending=False)
    for k, v in top3.items():
        print(f"   {k:32s} : {v} kali")

def rekomendasi(wins, df):
    print("\n" + "="*60)
    print("REKOMENDASI TARUHAN")
    print("="*60)

    # Berdasarkan win rate 100 race
    sorted_wins = sorted(wins.items(), key=lambda x: x[1], reverse=True)
    
    print("\nMode 'Siapa juaranya' (hadiah 5x):")
    print(f"   ★ Utama     : {sorted_wins[0][0]} ({sorted_wins[0][1]}%)")
    print(f"   Alternatif  : {sorted_wins[1][0]} / {sorted_wins[2][0]}")

    print("\nMode 'Siapa yang bukan juara' (hadiah 1.15x):")
    print(f"   ★ Utama     : {sorted_wins[-1][0]} (paling jarang juara)")
    print(f"   Alternatif  : {sorted_wins[-2][0]} / {sorted_wins[-3][0]}")

    # Form terkini
    if len(df) >= 5:
        print("\nForm 5 race terakhir (siapa yang sering bagus):")
        recent = df[KARAKTER].tail(5)
        score = (6 - recent).sum().sort_values(ascending=False)  # semakin tinggi semakin bagus
        for k, v in score.head(3).items():
            print(f"   {k:32s} : skor {v}")

def tambah_race(df):
    print("\n" + "-"*50)
    print("TAMBAH HASIL RACE BARU")
    print("Masukkan peringkat 1 sampai 6 untuk setiap karakter")
    print("(1 = Juara, 6 = Terakhir)")
    print("-"*50)

    hasil = []
    for nama in KARAKTER:
        while True:
            try:
                pos = int(input(f"  Posisi {nama}: "))
                if 1 <= pos <= 6:
                    hasil.append(pos)
                    break
                else:
                    print("     Masukkan angka 1-6 saja!")
            except:
                print("     Masukkan angka yang valid!")

    # Cek apakah peringkat unik
    if len(set(hasil)) != 6:
        print("\n⚠ Peringkat tidak unik! Ada angka yang sama. Data tidak disimpan.")
        return df

    new_row = dict(zip(KARAKTER, hasil))
    new_row["Waktu"] = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    df.to_csv(FILE_RIWAYAT, index=False)
    
    print("\n✓ Data berhasil disimpan!")
    return df

def update_statistik(wins):
    print("\nUpdate Statistik 100 Race Terakhir")
    print("Masukkan jumlah kemenangan baru (langsung Enter jika tidak berubah)")
    
    baru = {}
    for k in KARAKTER:
        current = wins.get(k, 0)
        val = input(f"  {k} (sekarang {current}): ").strip()
        if val == "":
            baru[k] = current
        else:
            try:
                baru[k] = int(val)
            except:
                baru[k] = current
                print("     Input tidak valid, tetap pakai nilai lama.")
    
    simpan_statistik(baru)
    print("\n✓ Statistik berhasil diupdate!")
    return baru

# ============================================================
# PROGRAM UTAMA
# ============================================================
def main():
    df = load_riwayat()
    wins = load_statistik()

    while True:
        print("\n" + "="*60)
        print("           ANALISIS BALAP BUILD - MENU")
        print("="*60)
        print("1. Lihat Analisis Lengkap")
        print("2. Lihat Rekomendasi Taruhan")
        print("3. Tambah Hasil Race Baru")
        print("4. Update Statistik 100 Race")
        print("5. Lihat Semua Riwayat")
        print("0. Keluar")
        print("-"*60)

        pilihan = input("Pilih menu (0-5): ").strip()

        if pilihan == "1":
            tampilkan_analisis(df, wins)
        elif pilihan == "2":
            rekomendasi(wins, df)
        elif pilihan == "3":
            df = tambah_race(df)
        elif pilihan == "4":
            wins = update_statistik(wins)
        elif pilihan == "5":
            print("\nSemua Riwayat:")
            print(df.to_string())
        elif pilihan == "0":
            print("\nTerima kasih! Data sudah tersimpan.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
