nome_func = input("Digite o nome do funcionário: ")
cargo = int(input("Digite o cargo: (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário) "))
salario_base = float(input("Digite o salário base: R$"))
hora_extra = int(input("Digite o total de horas extras trabalhadas: "))
falta = int(input("Digite o total de faltas no mês: "))
bonus = int(input("Recebeu bônus por desempenho? (1-Sim, 2-Não) "))

extra = hora_extra * (salario_base * 0.015)

def calcular_horas_extras(a, b):
    calcular_horas_extras = a + b
    return calcular_horas_extras

salario_extra = calcular_horas_extras(salario_base, extra)
print(salario_extra)