# Input
a = float(input("Masukkan a: "))
b = float(input("Masukkan b: "))
c = float(input("Masukkan c: "))

# Proses keputusan
if a == 0:
    print("Bukan persamaan kuadrat.")
else:
    D = b**2 - 4*a*c
    print(f"Diskriminan (D) = {D:.2f}")

    if D > 0:
        print("Memiliki dua akar real berbeda.")
    else:
        if D == 0:
            print("Memiliki satu akar real kembar.")
        else:
            print("Tidak memiliki akar real.")