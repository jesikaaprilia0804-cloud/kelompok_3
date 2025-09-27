print('='*75)
print("Halo semuanya selamat datang di Program kami dari Kelompok 3")
print("Program ini dibuat untuk membantu mengelola data obat di apotek")
print('='*75)

class Apotik:
    def __init__(self, nama_apotik, alamat):
        self.nama_apotik = nama_apotik
        self.alamat = alamat
        self.obat_dict = {}

    def tambah_obat(self, nama_obat, harga):
        self.obat_dict[nama_obat] = harga

    def tampilkan_obat(self):
        print("Daftar Obat di Apotik", self.nama_apotik)
        for nama, harga in self.obat_dict.items():
            print(f"- {nama} : Rp{harga}")

    def beli_obat(self, nama_pembeli, daftar_beli):
        total = 0
        for obat in daftar_beli:
            if obat in self.obat_dict:
                total += self.obat_dict[obat]
        print("Nama Pembeli :", nama_pembeli)
        print("Barang yang dibeli :", ", ".join(daftar_beli))
        print("Total Harga : Rp", total)


apotik = Apotik("Apotek Sehat", "Jl. Merdeka No. 10")
apotik.tambah_obat("Paracetamol", 5000)
apotik.tambah_obat("Amoxicillin", 10000)
apotik.tambah_obat("Vitamin C", 7000)

apotik.tampilkan_obat()

nama = input("Masukkan nama pembeli: ")
barang = input("Masukkan nama obat yang dibeli (pisahkan dengan koma): ").split(",")
barang = [b.strip() for b in barang]

apotik.beli_obat(nama, barang)
