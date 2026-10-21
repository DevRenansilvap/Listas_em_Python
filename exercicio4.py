num = [0]*9
cont_div = 0
for i in range(len(num)):
    num[i] = int(input("Digite um valor:"))
    cont_div = 0
    for j in range(1,num[i]+1):
        if num[i] % j == 0:
            cont_div+=1
    if cont_div == 2:
        print("Numero Primo")
        print(f"valor:{num[i]}")
        print(f"Indice:{i}")
print(num)
print("Fim Algoritmo!!!!")  