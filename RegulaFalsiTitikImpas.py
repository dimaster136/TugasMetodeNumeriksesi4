import math

# Nama  : Dimas Sandy
# NIM   : 20250040026
# Metode: Regula Falsi (Posisi Palsu)


def f(t):
    return 800 * math.exp(0.3 * t) - 2000 - 400 * t


a = 5.0
b = 6.0
tol = 0.00001
maks_iterasi = 100

print("=" * 85)
print("     PROGRAM METODE REGULA FALSI - TITIK IMPAS BIAYA CLOUD")
print("Nama : Dimas Sandy")
print("NIM  : 20250040026")
print("=" * 85)

print(f"{'Iterasi':<10}{'a':<15}{'b':<15}{'c':<15}{'f(c)':<20}")
print("-" * 85)

if f(a) * f(b) >= 0:
    print("Interval tidak memenuhi syarat metode Regula Falsi.")
else:
    for i in range(1, maks_iterasi + 1):
        fa = f(a)
        fb = f(b)

        # Rumus Metode Regula Falsi
        c = (fb * a - fa * b) / (fb - fa)
        fc = f(c)

        # Menampilkan output dengan format 4 angka di belakang koma
        print(
            f"{i:<10}{a:<15.4f}{b:<15.4f}"
            f"{c:<15.4f}{fc:<20.4f}"
        )

        # Cek kriteria penghentian iterasi
        if abs(fc) < tol:
            break

        # Pembaruan batas interval
        if fa * fc < 0:
            b = c
        else:
            a = c

    print("-" * 85)
    print(f"Titik impas (t) = {c:.4f} bulan")
    print(f"Nilai f(t)      = {f(c):.4f}")
    print("=" * 85)