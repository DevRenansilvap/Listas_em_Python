vetor = [0] * 5

for i in range(len(vetor)):
    vetor[i] = float(input("Digite um valor:"))
    while True:
        if vetor[i] <0:
            print("Valor invalido!!!")
            vetor[i] = float(input("Digite um valor:"))
        else:
            break

    if vetor[i] % 2  == 0:
        print(f"O Numero {vetor[i]}, Indice:{i+1} é Par")
    else:
        print(f"o Numero {vetor[i]}, Indice:{i+1} é Impar")

print("Fim do Algoritmo")
print(vetor)