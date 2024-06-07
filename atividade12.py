#Faça um programa que leia um numero inteiro positivo N e imprima todos os números naturais de 0 até N em ordem decrescente.

N = int(input("Digite um número: "))

for num in range(N,-1, -1):
    print(num)
