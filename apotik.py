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

obat = {
    "Paracetamol" : "Mengurangi rasa sakit kepala, dan meredakan demam",
    "Ibuprofen" : "Pereda nyeri dan penurun demam",
    "Maltofer" : "Mengatasi kekurangan zat besi",
    "Folarin" : "Suplemen Asam Folat",
    "Chlorpheniramine" : "Meredakan alergi",
    "Antasida Doen" : "Meredakan gejala asam lambung berlebih",
    "Lopamid" : "Mengobati masalah diare",
    "Antimo" : "Mengatasi dan mencegah mual",
    "Cataflam" : "Mengatasi nyeri sendi akibat asam urat",
    "Coxavit" : "Suplmen multivitamin untuk memelihara daya tubuh",
    "Methylprednisolone" : "Mengurangi peradangan tenggorokan"
}

pasien = str(input("Silahkan masukkan nama pasien : ")).lower()
umur_p = int(input("Silahkan masukkan umur pasien : "))
jk = str(input("Silahkan masukkan jenis kelamin pasien : ")).lower()
alamat_p = str(input("Silahkan masukkan alamat pasien : ")).lower()
keluhan_p = str(input("Silahkan masukkan keluhan pasien : ")).lower()
obat_p = str(input("Silahkan masukkan obat yang sudah di resepkan : ")).lower()

diagnosa_p = [
    ["Sakit kepala", "Demam"], ["Kelelahan", "wajah pucat", "Merawat janin"], ["Flu", "Badan gatal"],
    ["Maag", "Gerd"], ["BAB terus menerus", "BAB terlalu encer"], ["Mabuk perjalanan", "Mual selama perjalanan"],
    ["Asam urat kumat", "Nyeri sendi"], ["Menjaga imun tubuh", "Vitamin"],
    ["Sakit tenggorokan", "Radang Tenggorokan"]
]

print(f"Ini adalah data pasien : {pasien} \n{umur_p} \n{jk} \n{alamat_p}") #\n{keluhan_p} \n{obat_p}")
print(f"{keluhan_p} \n{diagnosa_p}")

if sakit in diagnosa_p == "Sakit Kepala":
    print(f"{obat}".obat.keys("Paracetamol"))
