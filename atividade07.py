#Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido


num1 = float(input("Digite um numero: "))
minimo = num1
maximo = num1

for i in range(9):
    numero = float(input(f"Digite outro numero: "))
    if numero < minimo:
        minimo = numero
    elif numero > maximo:
        maximo = numero

print(f"O menor valor lido é: {minimo}")
print(f"O maior valor lido é: {maximo}")
