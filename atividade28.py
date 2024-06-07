'''. O funcionário chamado Carlos tem um colega chamado João que recebe um salário
que equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta
de poupança e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao
mês. João aplicará seu salário integralmente no fundo de renda fixa, que está
rendendo 5% ao mês. Construa um programa que deverá calcular e mostrar a
quantidade de meses necessários para que o valor pertencente a João iguale ou
ultrapasse o valor pertencente a Carlos. Teste com outros valores para as taxas.'''


salario_carlos = float(input("Digite o salário de Carlos: "))
salario_joao = salario_carlos / 3

rendimento_carlos = 0.02 
rendimento_joao = 0.05  

meses = 0

while salario_joao < salario_carlos:
    salario_carlos *= (1 + rendimento_carlos)
    salario_joao *= (1 + rendimento_joao)
    meses = meses + 1

print("Após", meses, "meses, o valor pertencente a João igualará ou ultrapassará o valor pertencente a Carlos.")
