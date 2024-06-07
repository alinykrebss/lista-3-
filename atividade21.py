'''Faça um programa que receba dois números. Calcule o mostre:
a. A soma dos números pares desse intervalo de números, incluindo os números
digitados;
b. A multiplicação dos números impares desse intervalo, incluindo os digitados;'''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if num1 < num2:
    inicio = num1
    fim = num2
else:
    inicio = num2
    fim = num1

soma = 0
multiplicacao = 1

num = inicio
while num <= fim:
    if num % 2 == 0:  
        soma += num
    else: 
        multiplicacao *= num
    
    
    num += 1

print("Soma dos números pares:", soma)
print("Multiplicação dos números ímpares:", multiplicacao)


