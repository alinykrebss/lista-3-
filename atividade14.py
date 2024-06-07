#. Faça um programa que leia um número inteiro positivo par N e imprima todos os números pares de 0 até N em ordem decrescente.

n = int(input("Digite um número par: "))
if n %2 == 0:
    for num in range(n,-1, -2 ):
        print(num)
