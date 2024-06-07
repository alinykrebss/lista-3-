#Faça um programa que leia um numero inteiro positivo par N e imprima todos os números pares de 0 até N em ordem crescente.

N = int(input("Digite um número par: "))

for num in range(0, N, 2 ):
    print(num)