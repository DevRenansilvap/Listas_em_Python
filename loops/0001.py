n1= float(input("Digite o valor 1"))
n2 = float(input("Digite o valor 2"))

while True:
    print("""
    =OPÇÕES=
    [1] - somar
    [2] - multiplicar
    [3] - maior
    [4] - novos numeros
    [5] - sair
""")
    opicao= int(input("Qual o peração deseja Fazer com esses valores?"))

    if opicao == 1:
        print(n1+n2)
    elif opicao == 2:
        print(n1*n2)
    elif opicao == 3:
        if n1 > n2:
            print(f"o numero maior é{n1}")
        else:
            print(f"O Numero Maior é {n2}")
    elif opicao == 4:
        n1= float(input("Digite o valor 1"))
        n2 = float(input("Digite o valor 2"))
    elif opicao == 5:
        print("Encerrando Programa!!!")
        break
    else:
        print("Opção Invalida!!!")