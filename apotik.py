print("="*60)
print("   Program Pengelolaan Data Apotek - Kelompok 3")
print("="*60)

# Daftar obat, fungsi, dan harga
obat = {
    "Paracetamol": ("Mengurangi sakit kepala/demam", 5000),
    "Ibuprofen": ("Pereda nyeri & demam", 7000),
    "Maltofer": ("Mengatasi kekurangan zat besi", 10000),
    "Folarin": ("Suplemen Asam Folat", 8000),
    "Chlorpheniramine": ("Meredakan alergi/flu", 6000),
    "Antasida Doen": ("Meredakan asam lambung", 5000),
    "Lopamid": ("Mengobati diare", 7000),
    "Antimo": ("Mencegah mual & mabuk", 4000),
    "Cataflam": ("Mengatasi nyeri sendi/asam urat", 9000),
    "Coxavit": ("Suplemen multivitamin", 12000),
    "Methylprednisolone": ("Mengurangi radang tenggorokan", 11000)
}

# Keluhan → Obat
diagnosa_obat = {
    "sakit kepala": "Paracetamol",
    "demam": "Paracetamol",
    "kelelahan": "Maltofer",
    "wajah pucat": "Maltofer",
    "merawat janin": "Folarin",
    "flu": "Chlorpheniramine",
    "badan gatal": "Chlorpheniramine",
    "maag": "Antasida Doen",
    "gerd": "Antasida Doen",
    "bab terus menerus": "Lopamid",
    "bab terlalu encer": "Lopamid",
    "mabuk perjalanan": "Antimo",
    "mual selama perjalanan": "Antimo",
    "asam urat kumat": "Cataflam",
    "nyeri sendi": "Cataflam",
    "sakit tenggorokan": "Methylprednisolone",
    "radang tenggorokan": "Methylprednisolone",
    "vitamin": "Coxavit",
    "menjaga imun tubuh": "Coxavit"
}

# Riwayat pasien
riwayat = []

while True:
    print("\n=== INPUT DATA PASIEN ===")
    nama = input("Nama pasien : ").title()
    umur = int(input("Umur pasien : "))
    jk = input("Jenis kelamin : ").title()
    alamat = input("Alamat pasien : ").title()

    print("\nDaftar diagnosa yang tersedia:")
    for d in diagnosa_obat.keys():
        print("-", d.title())

    keluhan_list = []
    obat_list = []
    total_harga = 0

    for i in range(3):  # Maksimal 3 keluhan
        keluhan = input(f"\nMasukkan keluhan {i+1} (atau tekan Enter jika selesai): ").lower()
        if keluhan == "":  
            break
        if keluhan in diagnosa_obat:
            nama_obat = diagnosa_obat[keluhan]
            fungsi, harga = obat[nama_obat]
            keluhan_list.append(keluhan)
            obat_list.append((nama_obat, fungsi, harga))
            total_harga += harga
        else:
            print("❌ Keluhan tidak ditemukan.")

    print("\n=== HASIL DIAGNOSA ===")
    for o in obat_list:
        print(f"Obat : {o[0]} | Fungsi : {o[1]} | Harga : Rp{o[2]}")
    print(f"Total harga : Rp{total_harga}")

    # Input uang
    bayar = int(input("Masukkan jumlah uang pasien : Rp"))
    if bayar >= total_harga:
        kembalian = bayar - total_harga
        print(f"✅ Pembayaran berhasil, kembalian : Rp{kembalian}")
    else:
        print("❌ Uang tidak cukup!")
        kembalian = 0

    # Simpan ke riwayat
    riwayat.append({
        "nama": nama,
        "umur": umur,
        "jk": jk,
        "alamat": alamat,
        "keluhan": keluhan_list,
        "obat": [o[0] for o in obat_list],
        "total": total_harga,
        "bayar": bayar,
        "kembalian": kembalian
    })

    ulang = input("\nTambah pasien lagi? (y/n): ").lower()
    if ulang != "y":
        break

# Tampilkan riwayat
print("\n=== RIWAYAT PASIEN ===")
for r in riwayat:
    print(f"{r['nama']} | Keluhan: {', '.join(r['keluhan'])} | Obat: {', '.join(r['obat'])} | Total: Rp{r['total']}")
