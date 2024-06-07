#Faça um programa que leia um número inteiro positivo par N e imprima todos os
#números impares de 1 até N em ordem crescente.

N = int(input("Digite um número par: "))

for num in range(1, N, 2):
    print(num)
