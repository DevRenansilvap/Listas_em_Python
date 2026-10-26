vetor = [0]*10
count_par = 0
count_impar = 0

for i in range(len(vetor)):
    vetor[i] = int(input("Qual o numero a ser adicionado no vetor?"))
    for j in vetor:
        if j % 2 == 0 :
            count_par+=1
        else:
            count_impar+=1

print(f"Quantidade de Pares:{count_par}")
print(f"Quantidade de Impar:{count_impar}")