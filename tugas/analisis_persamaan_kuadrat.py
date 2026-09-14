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
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print(f"Dua akar real: x1 = {x1:.2f}, x2 = {x2:.2f}")
    else:
        if D == 0:
            x = -b / (2*a)
            print(f"Akar real kembar: x = {x:.2f}")
        else:
            print("Tidak ada akar real.")