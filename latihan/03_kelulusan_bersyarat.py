# Input
nilai = float(input("Masukkan nilai: "))
kehadiran = float(input("Masukkan persentase kehadiran: "))

# Proses keputusan
if nilai >= 60 and kehadiran >= 80:
    print("Lulus")
else:
    print("Belum lulus")