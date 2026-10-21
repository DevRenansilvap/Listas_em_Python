nota = [0]*10
cont_aprovado = [0]
cont_reprovado = [0]

for i in range(len(nota)):
    while True:
        nota[i] = float(input("Digite Sua Nota:"))
        if nota[i] > 0:
            break
        else:
            print("Nota Invalida!!!")
            nota[i] = float(input("Digite Sua Nota:"))


    if nota[i] < 4:
        print(f"Aluno {i+1} Reprovado")
        cont_reprovado+=1
    elif nota[i] >=7:
        print(f"Aluno {i+1} Aprovado")
        cont_aprovado+=1
    else:
        print(f"Aluno {i+1} - AF (Avaliação Final)")

print(nota)
print(f"Quantidade de Aprovados {cont_aprovado}")
print(f"Quantidade de Reprovados {cont_reprovado}")
print("Fim do Programa")