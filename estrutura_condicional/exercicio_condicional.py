import os
os.system('clear')

peso = float(input("Qual é o seu peso?"))

os.system('clear')

altura = float(input("qual a sua altura?"))

os.system('clear')

imc = peso / altura**2

print(f"Seu IMC é igual á:{imc:.2f}")

os.system('clear')

if imc >= 25:
    print('excesso de Peso "gordito"')
else:
    print('Voce esta magro "Magrito"')  