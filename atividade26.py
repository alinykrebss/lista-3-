'''Faça um algoritmo que encontre o primeiro múltiplo de 11, 13 ou 17 após um número
dado.'''

num = int(input("Digite um número: "))

multiplo = num + 1


while True:
    if multiplo % 11 == 0 or multiplo % 13 == 0 or multiplo % 17 == 0:
        break
    multiplo = multiplo + 1 


print("O primeiro múltiplo de ", num, "é:", multiplo)
