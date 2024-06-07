''' Chico tem 1.50 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.10 metros e
cresce 3 centímetros por ano. Escreva um programa que calcule e imprima quantos
anos serão necessários para que Zé seja maior que Chico.
'''
altura_chico = 1.50 
altura_ze = 1.10  
crescimento_chico = 0.02
crescimento_ze = 0.03  
anos = 0  

while altura_ze <= altura_chico:
    altura_chico += crescimento_chico
    altura_ze += crescimento_ze
    anos += 1


print("Serão necessários", anos, "anos para que Zé seja maior que Chico.")
