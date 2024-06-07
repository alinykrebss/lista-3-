'''Ler uma sequência de números inteiros e determinas se eles são pares ou não. Deverá
ser informado o número de dados lidos e números de valores pares. O processo
termina quando for digitado o número 1000.
'''
contador = 0  
par = 0     

while True:
    numero = int(input("Digite um número inteiro (ou 1000 para sair): "))
    
    
    if numero == 1000:
        break
    
    
    if numero % 2 == 0:
        par = par + 1 
    
    contador = contador + 1

print(f"Número de dados lidos: {contador}")
print(f"Número de valores pares: {par}")
