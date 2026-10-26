produtos = [1,2,3,4,5,6,7,8,9,10]
quantidade=[4,2,3,6,5,8,6,4,9,7]

while True:
    cod = int(input("Qual o codigo do produto?"))
    if cod == 0:
        print("Fim Do Programa""")
        break
    else:
        #Percorrer Produtos
        encontrado = False
        for i in range(len(produtos)):
            if produtos[i] == cod:
                encontrado = True
                qtd=int(input("Qual a quantidade que voce me deseja senhor?"))
                if qtd <= quantidade[i]:
                    quantidade[i]-=qtd
                    print("Na hora meu patrao ta na mao!!")
                elif qtd > quantidade[i]:
                    print(f"Tem, mas essa quantidade nao viu major, temos somente: {quantidade[i]}!!")
                else:
                    print("Quantidade invalida Patron")
        if not encontrado:
            print("Codigo de Produto nao existente ")
for i in range(len(produtos)):
    print(f" Codigo Produtos: {produtos[i]} Quantidade: {quantidade[i]}")