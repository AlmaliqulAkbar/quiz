
class Karyawan:
    def __init__(self, nama, jabatan, gaji_harian):
        self.nama = nama
        self.jabatan = jabatan
        self.gaji_harian = gaji_harian

    def tampilkan_data(self):
        print("Nama Karyawan :", self.nama)
        print("Jabatan       :", self.jabatan)
        print("Gaji Harian   :", self.gaji_harian)

    def hitung_gaji(self, hari_kerja):
        return self.gaji_harian * hari_kerja

    def hitung_bonus(self, hari_kerja):
        if hari_kerja >= 25:
            return 200000
        else:
            return 0

    def total_gaji(self, hari_kerja):
        return self.hitung_gaji(hari_kerja) + self.hitung_bonus(hari_kerja)
