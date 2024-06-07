'''Escreva um programa completo que permita a qualquer aluno introduzir pelo teclado,
uma sequencia arbitraria de notas (validas no intervalo de 10 a 20) e que mostre na
tela, como resultado, a correspondente média aritmética. O numero de notas que o
aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminara
quando for introduzido um valor que não seja valido como nota de aprovação.
'''
notas = []

while True:
    nota = float(input("Digite uma nota entre 10 e 20 (digite uma nota fora desse intervalo para parar): "))
    
    if 10 <= nota <= 20:
        notas.append(nota)  
    else:
        break  

if notas:
    total = 0
    quantidade_notas = 0
    for nota in notas:
        total = total + nota
        quantidade_notas += 1
    
    media = total / quantidade_notas
    print("A média das notas é:", media)
else:
    print("Nenhuma nota válida foi inserida.")
