n = int(input("Digite um número inteiro positivo: "))
soma = 0

if n > 0:
    for i in range(1, n + 1):
        soma += i

    print("A soma dos", n, "primeiros números naturais é:", soma)
else:
    print("Por favor, digite um número inteiro positivo.")
