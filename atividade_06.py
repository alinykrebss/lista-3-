'''Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima
sua média.'''

soma = 0
positivos = 0

for _ in range(10):#o _ vai pra algum lugar pode colocar ate paralelipipedo
    numero = int(input("Digite um número inteiro: "))
    if numero > 0:
        soma += numero
        positivos += 1

if positivos > 0:
    media = soma / positivos
    print(f"A média dos números positivos é: {media}")

else:
    print("nenhum numero positivo foi digitado")
    