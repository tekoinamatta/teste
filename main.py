altura = int(input("Altura: "))
espaco_branco = altura - 1

for i in range(1, altura + 1):
    print(" " * espaco_branco, "*" * i)
    espaco_branco -= 1