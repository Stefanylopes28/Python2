def calcular_media(nota1, nota2, nota3):
    media = round((nota1 + nota2 + nota3) / 3, 2)

    print("=== Boletim Escolar ===")
    print(f"Nota 1: {nota1:.2f}")
    print(f"Nota 2: {nota2:.2f}")
    print(f"Nota 3: {nota3:.2f}")
    print(f"Média Final: {media:.2f}")

if __name__ == "__main__":
    nota1 = 7.5
    nota2 = 8.0
    nota3 = 6.5

    calcular_media(nota1, nota2, nota3)
