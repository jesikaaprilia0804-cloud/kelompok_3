print('='*75)
print("Halo semuanya selamat datang di Program kami dari Kelompok 3")
print("Program ini dibuat untuk membantu mengelola data obat di apotek")
print('='*75)

class Apotik:
    def __init__(self, nama_apotik, alamat):
        self.nama_apotik = nama_apotik
        self.alamat = alamat

class Obat(Apotik):
    def __init__(self, nama_obat, fungsi_obat):
        self.nama_obat = nama_obat
        self.fungsi_obat = fungsi_obat

class Pasien(Apotik):
    def __init__(self, nama, umur, jenis_k, alamat_pasien, keluhan, diagnosa, obat_dibeli):
        self.nama = nama
        self.umur = umur
        self.jenis_k = jenis_k
        self.alamat_pasien = alamat_pasien
        self.keluhan = keluhan
        self.diagnosa = diagnosa
        self.obat_dibeli = obat_dibeli

class Administrasi(Apotik):
    def __init__(self, total_harga, kembalian):
        self.total_harga = total_harga
        self.kembalian = kembalian

# Daftar obat dan fungsinya
obat = {
    "Paracetamol" : "Mengurangi rasa sakit kepala, dan meredakan demam",
    "Ibuprofen" : "Pereda nyeri dan penurun demam",
    "Maltofer" : "Mengatasi kekurangan zat besi",
    "Folarin" : "Suplemen Asam Folat",
    "Chlorpheniramine" : "Meredakan alergi dan flu",
    "Antasida Doen" : "Meredakan gejala asam lambung berlebih",
    "Lopamid" : "Mengobati masalah diare",
    "Antimo" : "Mengatasi dan mencegah mual",
    "Cataflam" : "Mengatasi nyeri sendi akibat asam urat",
    "Coxavit" : "Suplemen multivitamin untuk memelihara daya tubuh",
    "Methylprednisolone" : "Mengurangi peradangan tenggorokan"
}

# Mapping keluhan -> obat
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

# Input pasien
nama = str(input("Silahkan masukkan nama pasien : ")).title()
umur = int(input("Silahkan masukkan umur pasien : "))
jk = str(input("Silahkan masukkan jenis kelamin pasien : ")).lower()
alamat_pasien = str(input("Silahkan masukkan alamat pasien : ")).title()

print("\nDaftar diagnosa yang tersedia:")
for d in diagnosa_obat.keys():
    print("-", d.title())

keluhan = str(input("\nSilahkan masukkan keluhan pasien (sesuai daftar): ")).lower()

# Proses diagnosa
if keluhan in diagnosa_obat:
    nama_obat = diagnosa_obat[keluhan]
    fungsi = obat.get(nama_obat, "Fungsi obat tidak ditemukan")

    # buat object pasien
    pasien = Pasien(nama, umur, jk, alamat_pasien, keluhan, keluhan, nama_obat)

    print("\n=== DATA PASIEN ===")
    print(f"Nama     : {pasien.nama}")
    print(f"Umur     : {pasien.umur}")
    print(f"JK       : {pasien.jenis_k}")
    print(f"Alamat   : {pasien.alamat_pasien}")
    print(f"Keluhan  : {pasien.keluhan}")
    print("\n=== HASIL DIAGNOSA ===")
    print(f"Obat diresepkan : {pasien.obat_dibeli}")
    print(f"Fungsi obat     : {fungsi}")
else:
    print("Keluhan tidak ada di daftar diagnosa, silakan konsultasi lebih lanjut.")
