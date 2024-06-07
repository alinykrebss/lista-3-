'''Escreva um programa que receba como entrada o valor do saque realizado pelo cliente
de um banco e retorne quantas notas de cada valor serão necessárias para atender ao
saque com a menor quantidade de notas possível. Serão utilizadas notas de 200, 100,
50, 20, 10, 5, 2 e 1 real.'''

def ler():
    valor = float(input("digite o valor: "))
    return valor

def qtd_notas(valor, nota):
    if valor >= nota:
        qtd = valor // nota
        valor = valor - (qtd * nota)
        print(f"{qtd} notas de R$ {nota:.2f}")
    return valor

notas = [200, 100, 50, 20, 10, 5, 2, 1]

valor = ler()
for nota in notas:
    valor = qtd_notas(valor, nota)

print(" obrigada pela referencia, volte amanha")

