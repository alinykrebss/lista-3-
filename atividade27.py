'''Faça um programa que some os termos de valor par da sequencia de Fibonacci, cujos
valores não ultrapassem quatro milhões.'''

fibo_atual = 1
fibo_proximo = 2


pares = 0

while fibo_atual <= 4000000:
    if fibo_atual % 2 == 0:
        pares += fibo_atual
    
    fibo_atual, fibo_proximo = fibo_proximo, fibo_atual + fibo_proximo

print("A soma dos termos de valor par da sequência de Fibonacci são:", pares)
