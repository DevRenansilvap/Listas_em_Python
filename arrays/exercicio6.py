qtd = 2

nome_produtos= [""]*qtd
qtd_produtos= [""]*qtd
preco_produtos= [""]*qtd
total_vendas=0
for i in range(qtd):
    nome_produtos[i] = input (f"Nome do produto {i+1}: ")
    qtd_produtos[i] = int(input(f"Quantidade do {i+1} produto: "))
    preco_produtos[i] = float(input(f"Preço unitario do produto {i+1}: "))

for i in range(len(nome_produtos)):
    print("="*80)
    print(f"O Produto {nome_produtos[i]} Quantidade:{qtd_produtos[i]} Preço do Produto:{preco_produtos[i]} Valor Total em vendas:{qtd_produtos[i]*preco_produtos[i]}")
    print("="*80)
    total_vendas+=(qtd_produtos[i]*preco_produtos[i])

print("-"*80)
print(f"Seu Salario é de R$:545,00 | A comissao foi:{total_vendas} | Total:{(total_vendas*0.05)+545}")
print("-"*80)
#vendedor Recebe 545 + 5% do valor das vendas