print("Simulador de parcelas")
juros = 0
emprestimo =  float(input("Emprestimo desejado"))
while True:
    parcelas =  int(input("Qauntidades de Parcelas"))
    if (parcelas < 1 or parcelas > 12):
        print("Quantidades de Parcelas Invalidas!")
    else:
        if (parcelas >= 1 and parcelas >=2):
            juros = emprestimo*0.02
        elif ( parcelas >=3 and parcelas <6):
            juros = emprestimo*0.1
        elif (parcelas >=6 and parcelas <9):
            juros = emprestimo*0.15
        elif (parcelas >= 9 and parcelas <12):
            juros = emprestimo*0.2
        else:
            juros = emprestimo*0.25

        total = emprestimo + juros
        valor_parcelas = total/parcelas

        print(f""" 
        Total = total:{total:.2f} | juros = R${juros:.2f} | 
        """)
        break