#Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.

soma = 0
for num in range(0,52,2):
    soma += num
    print(num)
print(f"soma é de {soma}")
