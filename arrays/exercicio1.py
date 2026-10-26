rodadas = int(input("Quantas Rodadas"))
pontos_jogador1 = 0
pontos_jogador2 = 0
v_j1 = 0
v_j2 = 0
empates = 0
for i in range(rodadas):
    for i in range(5):
            pontos1 = int(input("Quanl a pontuação do jogador 1?"))
            if pontos1 <0 or pontos1 > 100:
                print("Pontuação invalida!!! tente novamente")
                pontos1 = int(input("Quanl a pontuação do jogador 1?"))
            else:
                pontos_jogador1 += pontos1
            pontos2 = int(input("Qual a pontuação do jogador 2?"))
            if pontos1 <0 and pontos1 > 100:
                print("Pontuação invalida!!! tente novamente")
                pontos1 = int(input("Quanl a pontuação do jogador 1?"))
            else:
                pontos_jogador2 += pontos2
                if pontos1 == pontos2:
                    print(f"Rodada {i+1} Empatou!!")
                    empates +=1
                elif pontos1 > pontos2:
                    print(f"jogador 1 venceu a rodada{i}")
                    v_j1 +=1
                else:
                    print(f"jogador 2 venceu a rodada{i}")
                    v_j2 +=1


print(f"""
O Jogador 1 teve {pontos1} Pontos e  venceu {v_j1} Rodadas!
O Jogador 2 teve {pontos2} Pontos e  venceu {v_j2} Rodadas!
Houve {empates} Empates!

""")            

