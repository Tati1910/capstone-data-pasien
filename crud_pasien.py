# crud_pasien.py
import pandas as pd
import os

CSV_FILE = "patients.csv"

# Pastikan file CSV ada (kalau belum, buat header kosong)
if not os.path.exists(CSV_FILE):
    df_empty = pd.DataFrame(columns=["ID", "Nama", "Umur", "Jenis_Kelamin", "Poli", "Tanggal_Masuk"])
    df_empty.to_csv(CSV_FILE, index=False)

def load_data():
    """Baca file CSV dan kembalikan DataFrame."""
    return pd.read_csv(CSV_FILE, dtype=str)  # baca sebagai string supaya aman

def save_data(df):
    """Simpan DataFrame ke CSV."""
    df.to_csv(CSV_FILE, index=False)

def next_id(df):
    """Buat ID unik otomatis (angka)."""
    if df.empty:
        return "1"
    # pastikan konversi aman
    try:
        nums = [int(x) for x in df["ID"].dropna().astype(str) if x.isnumeric()]
        return str(max(nums) + 1) if nums else "1"
    except Exception:
        return str(len(df) + 1)

def tambah_pasien():
    df = load_data()
    id_baru = next_id(df)
    print(f"ID pasien otomatis: {id_baru}")
    nama = input("Nama: ").strip()
    umur = input("Umur: ").strip()
    jk = input("Jenis Kelamin: ").strip()
    poli = input("Poli: ").strip()
    diagnosa = input("diagnosa: ").strip()
    lama_rawat = input("lama_rawat: ").strip()
    biaya = input("biaya: ").strip()
    status_pulang = input("status_pulang: ").strip()
    tanggal_masuk = input("Tanggal Masuk (YYYY-MM-DD): ").strip()

    # tambahkan baris baru
    df.loc[len(df)] = [id_baru, nama, umur, jk,  poli, diagnosa, lama_rawat, biaya, status_pulang, tanggal_masuk]
    save_data(df)
    print("Data berhasil ditambahkan.\n")

def lihat_data():
    df = load_data()
    if df.empty:
        print("Belum ada data.\n")
    else:
        print("\n=== Daftar Pasien ===")
        # tampil rapi tanpa index
        print(df.to_string(index=False))
        print()

def update_pasien():
    df = load_data()
    if df.empty:
        print("belum ada data.\n")
        return
    id_target = input("masukkan id_pasien yang ingin diupdate: ").strip()
    if id_target not in df["id_pasien"].astype(str).values:
        print("id_pasien tidak ditemukan.\n")
        return
    print("kolom yang bisa diupdate: id_pasien, nama, umur, jenis_kelamin, poli, diagnosa, lama_rawat, biaya, status_pulang, tanggal_masuk")
    kolom = input("pilih kolom: ").strip()
    if kolom not in df.columns:
        print("kolom tidak valid.\n")
        return
    nilai = input("masukkan nilai baru: ").strip()
    df.loc[df["id_pasien"].astype(int) == id_target, kolom] = nilai
    save_data(df)
    print("data berhasil diupdate.\n")

    # save dan ubah baris ini
    df.to_csv(CSV_FILE, index=False)
    print("Perubahan telah disimpan ke file patients.csv")
    
    

def hapus_pasien():
    df = load_data()
    if df.empty:
        print("belum ada data.\n")
        return
    id_target = input("Masukkan id_pasien yang ingin dihapus: ").strip()
    if id_target not in df["id_pasien"].astype(str).values:
        print("id_pasien tidak ditemukan.\n")
        return
    # konfirmasi sederhana
    yakin = input(f"Yakin hapus id_pasien {id_target}? (y/n): ").lower()
    if yakin == "y":
        df = df[df["id_pasien"].astype(str)== id_target]
        save_data(df)
        print("Data berhasil dihapus.\n")
    else:
        print("Pembatalan hapus.\n")

    

def menu():
    while True:
        print("=== MENU CRUD DATA PASIEN ===")
        print("1. Tambah")
        print("2. Lihat")
        print("3. Update")
        print("4. Hapus")
        print("5. Keluar")
        pilihan = input("Pilih (1-5): ").strip()
        if pilihan == "1":
            tambah_pasien()
        elif pilihan == "2":
            lihat_data()
        elif pilihan == "3":
            update_pasien()
        elif pilihan == "4":
            hapus_pasien()
        elif pilihan == "5":
            print("Selesai. Terima kasih.")
            break
        else:
            print("Pilihan tidak valid.\n")

if __name__ == "__main__":
    menu()
