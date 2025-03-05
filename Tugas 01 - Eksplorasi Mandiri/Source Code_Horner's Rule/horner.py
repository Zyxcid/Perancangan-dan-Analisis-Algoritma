def horner_rule(coefficients, x):
    hasil = coefficients[0]
    for i in range(1, len(coefficients)):
        hasil = hasil * x + coefficients[i]
    return hasil

# Contoh penggunaan
koefisien = [2, -6, 2, -1]  # P(x) = 2x³ - 6x² + 2x - 1
x_nilai = 3
hasil = horner_rule(koefisien, x_nilai)
print(f"Hasil evaluasi polinomial: {hasil}")