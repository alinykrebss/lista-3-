'''Faça um algoritmo que leia um numero positivo e imprima seus divisores.
'''
num = int(input("Digite um número positivo: "))


if num <= 0:
    print("O número digitado não é positivo.")
    
else:
    print("Divisores de", num, ":")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


