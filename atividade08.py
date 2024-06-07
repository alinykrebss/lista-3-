#Faça um programa que leia 10 inteiros e imprima sua média.
soma = 0
for i in range(10):
    numero = int(input("Digite um número inteiro: "))
    soma += numero

media = soma / 10
print("A média dos números é:", media)
