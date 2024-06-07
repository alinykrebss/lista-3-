#Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes. A primeira vez deve usar a estrutura de repetição for, a segunda while.
print("utilizando for")

for n in range (0, 101):
    print(f"{n}")

print("utilizando while")

limite = 0

while limite <= 100:
    print(f"{limite}")
    limite += 1
