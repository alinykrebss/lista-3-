'''Escreva um programa que leia um numero inteiro e calcule a soma de todos os
divisores desse número, com exceção dele próprio. Ex: a soma dos divisores do
numero 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
'''
num = int(input("Digite um número inteiro: "))

soma = 0


for x in range(1 , num ):
    if num % x == 0:
        soma = soma + x

print("A soma dos divisores de", num, "é:", soma)
