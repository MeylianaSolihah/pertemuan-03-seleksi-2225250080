# Input
a = float(input("Sisi a: "))
b = float(input("Sisi b: "))
c = float(input("Sisi c: "))

# Validasi sisi
if a > 0 and b > 0 and c > 0:
    if a + b > c and a + c > b and b + c > a:
        # Klasifikasi segitiga
        if a == b and b == c:
            print("Segitiga sama sisi.")
        else:
            if a == b or a == c or b == c:
                print("Segitiga sama kaki.")
            else:
                print("Segitiga sembarang.")
    else:
        print("Bukan segitiga.")
else:
    print("Bukan segitiga.")