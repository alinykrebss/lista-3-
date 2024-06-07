#Faça um programa que leia um numero inteiro N e depois imprima os N primeiros números naturais impares.

N = int(input("Digite um número inteiro N: "))

for num in range(1, 2*N, 2):
    print(num)


