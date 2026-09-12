import sys
from deep_translator import GoogleTranslator
from rich.console import Console
from rich.table import Table
from rich.live import Live
from rich.panel import Panel

console = Console()

def terjemahkan_teks(teks, dari_bahasa='id', ke_bahasa='en'):
    try:
        translator = GoogleTranslator(source=dari_bahasa, target=ke_bahasa)
        return translator.translate(teks)
    except Exception as e:
        return f"Terjadi kesalahan: {e}"

if __name__ == "__main__":
    # 1. Judul di luar tabel sesuai permintaan Anda
    console.print("\n[bold cyan]=== PROGRAM PENERJEMAH MULTI-BAHASA ===[/]", justify="center")
    console.print("[italic yellow]Ketik 'keluar' pada kolom teks untuk berhenti.[/]\n", justify="center")

    # Inisialisasi struktur tabel utama
    tabel_utama = Table(show_lines=True, header_style="bold magenta")
    tabel_utama.add_column("Sesi / Proses", style="cyan", width=25)
    tabel_utama.add_column("Detail / Input / Hasil", style="white", width=45)

    # Menampilkan tabel secara LIVE agar bisa terus diperbarui
    with Live(tabel_utama, console=console, refresh_per_second=4):
        
        # --- PROSES INPUT BAHASA ---
        # Menggunakan input manual sementara di luar live render agar tidak bentrok
        pass 

    # Karena Rich Live membatasi input standar, kita susun baris demi baris secara rapi:
    
    # Baris Panduan Bahasa
    tabel_utama.add_row("Panduan Kode Bahasa", "id (Indo), en (Inggris), ja (Jepang), ko (Korea)")
    console.print(tabel_utama)

    # Input Bahasa Asal
    src_lang = console.input("[bold green]▶ Masukkan Kode Bahasa ASAL: [/]").strip().lower() or 'id'
    tabel_utama.add_row("Bahasa Asal", f"[yellow]{src_lang.upper()}[/]")
    
    # Bersihkan layar bawah dan cetak ulang tabel yang terupdate
    console.clear()
    console.print("\n[bold cyan]=== PROGRAM PENERJEMAH MULTI-BAHASA ===[/]", justify="center")
    console.print(tabel_utama)

    # Input Bahasa Tujuan
    target_lang = console.input("[bold green]▶ Masukkan Kode Bahasa TUJUAN: [/]").strip().lower() or 'en'
    tabel_utama.add_row("Bahasa Tujuan", f"[yellow]{target_lang.upper()}[/]")
    
    console.clear()
    console.print("\n[bold cyan]=== PROGRAM PENERJEMAH MULTI-BAHASA ===[/]", justify="center")
    console.print(tabel_utama)

    # --- PERULANGAN INPUT TEKS & HASIL ---
    hitung = 1
    while True:
        teks_input = console.input(f"\n[bold white]Masukkan Teks ke-{hitung}: [/]")
        
        if teks_input.lower() == 'keluar':
            tabel_utama.add_row("[bold red]Status[/]", "[bold red]Program Selesai. Terima Kasih![/]")
            console.clear()
            console.print("\n[bold cyan]=== PROGRAM PENERJEMAH MULTI-BAHASA ===[/]", justify="center")
            console.print(tabel_utama)
            break
            
        if not teks_input.strip():
            continue
            
        # Proses Terjemahan
        hasil = terjemahkan_teks(teks_input, dari_bahasa=src_lang, ke_bahasa=target_lang)
        
        # Masukkan Input dan Hasil ke dalam tabel secara berpasangan
        tabel_utama.add_row(f"Teks Asli ({hitung})", f"[dim white]{teks_input}[/]")
        tabel_utama.add_row(f"Hasil Terjemahan ({hitung})", f"[bold green]{hasil}[/]")
        
        # Cetak ulang tabel agar selalu rapi ke bawah
        console.clear()
        console.print("\n[bold cyan]=== PROGRAM PENERJEMAH MULTI-BAHASA ===[/]", justify="center")
        console.print(tabel_utama)
        
        hitung += 1
