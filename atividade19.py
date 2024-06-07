''' Escreva um algoritmo que leia um numero inteiro entre 100 e 999 e imprima na saída
cada um dos algarismos que compõem o número.
'''
numero = int(input("Digite um número inteiro entre 100 e 999: "))

if numero > 100 and numero < 999:
    # Extrai cada nmero
    centenas = numero // 100
    dezenas = (numero // 10) % 10
    unidades = numero % 10

else:
    print("digita certo desgraça")

print("Centenas:", centenas)
print("Dezenas:", dezenas)
print("Unidades:", unidades)
 