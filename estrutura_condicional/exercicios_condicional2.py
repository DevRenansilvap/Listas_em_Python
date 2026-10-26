n1 = float(input("Entre com a nota 1:"))
n2 = float(input("Entre com a nota 2:"))
media = (n1 + n2)/2
if media >=10:
    print("Aprovado")
elif media >7:
    print("Final")
elif media > 4:
    print("Reprovado")