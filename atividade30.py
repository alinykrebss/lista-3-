'''0. Um funcionário receber aumento anual. Em 1995 foi contratado por 2000 reais. Em
1996 recebeu um aumento de 1,5%. A partir de 1997, os aumentos sempre
correspondem ao dobro do ano anterior. Faça um programa que determine o salário
atual do funcionário.'''

salario = 2000
aumento = salario * 0.015
salario = salario + aumento

for ano in range(1997, 2023):
    aumento *= 2
    salario = salario + aumento

print("O salário atual do funcionário em 2022 é de R$", salario)
