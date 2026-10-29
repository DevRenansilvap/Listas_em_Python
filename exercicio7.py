produtos = []
quantidade=[]
count=0
while True:
    usuario= int(input("""
    ===========================================================
                        Painel Para:
                        CLIENTE = 1
                        ADMIN = 2
                        Sair = 0
    ===========================================================
"""))
    if usuario == 2 :
        count=3
        for x in range(count):
            senha = int(input("Digite a senha: "))
            if senha != 12345:
                count-=1
                print(f"Senha invalida!!! Tentativas Restantes:{count}")
                    
            else:
                while True:
                    opcao=int(input("Login Aceita o que deseja fazer:\n"
                                    "1 - Adicionar Produtos\n"
                                    "2 - Excluir Produtos\n" 
                                    "3 - sair\n"))
                    if opcao == 1:
                        qtd_produtos=int(input("Digite a Quantidade de Produtos que voce Quer adicionar: "))
                        for j in range(qtd_produtos):
                            produto=int(input("Qual o codigo do produto que voce quer adicionar?"))
                            produtos.append(produto)
                            qtd_quantidade = int(input("Qual a quantidade: "))
                            quantidade.append(qtd_quantidade)

                    elif opcao == 2:
                        print(f"Lista de Produtos: {produtos}")
                        ind_produto=int(input("Qual item da lista voce deseja remover?"))
                        produtos.pop(ind_produto)
                        print(f"Feito!! Lista atualizada: {produtos}")

                    elif opcao == 3:
                        print("Saindo do Painel Admin...")
                        usuario= 0
                        break
                break
    elif usuario == 1:
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
    elif usuario == 0:
        print("Encerrando Programa Major Uma Excelente semanda!!!")
        break
    else:
        print("Painel invalido amigo tente Novamente Major!!")
for i in range(len(produtos)):
    print(f" Codigo Produtos: {produtos[i]} Quantidade: {quantidade[i]}")