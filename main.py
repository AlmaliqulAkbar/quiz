
from karyawan import Karyawan

jumlah_karyawan = int(input("Jumlah Karyawan : "))

for i in range(jumlah_karyawan):
    print(f"\nKaryawan ke-{i + 1}")

    nama = input("Nama Karyawan : ")
    jabatan = input("Jabatan       : ")
    gaji_harian = int(input("Gaji Harian   : "))
    hari_kerja = int(input("Hari Kerja    : "))

    karyawan = Karyawan(nama, jabatan, gaji_harian)

    gaji_pokok = karyawan.hitung_gaji(hari_kerja)
    bonus = karyawan.hitung_bonus(hari_kerja)
    total = karyawan.total_gaji(hari_kerja)

    print("\n=== SLIP GAJI ===")
    print("Nama Karyawan :", karyawan.nama)
    print("Jabatan       :", karyawan.jabatan)
    print("Gaji Pokok    : Rp{:,.0f}".format(gaji_pokok).replace(",", "."))
    print("Bonus         : Rp{:,.0f}".format(bonus).replace(",", "."))
    print("Total Gaji    : Rp{:,.0f}".format(total).replace(",", "."))
