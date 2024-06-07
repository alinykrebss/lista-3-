#Faça um programa que peça ao usuário digitar 10 valores e some-os;

soma = 0 

for _ in range(10):
    num = int(input("Digite um número: "))
    if num > 0:
        soma += num

print(f"A soma dos números é: {soma}")
