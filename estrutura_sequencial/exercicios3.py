peso = float(input("Qual o seu peso?"))
altura = float(input("Qual a sua altura?"))
sexo = float(input("""
qual o seu sexo ?
1 - Homen
2 - Mulher
"""))

if sexo == 1:
    peso_homen = ((72.7 * altura) - 58)
    print(f"Seu pesom ideal é igual a:{peso_homen:.2f}")
elif sexo == 2:
    peso_mulher = ((62.1* altura) - 44,7)
    print(f"Seu peso ideal é igual a:{peso_mulher:.2f}")
else:
    print("Sexo Invalido")
    