def calcular_horas_extras(salario, extras):
    total_extras = (salario * 0.015) * extras
    return total_extras

def calcular_descontos_faltas(salario, faltas):
    descontos_falta = (salario * 0.02) * faltas
    return descontos_falta

def calcular_bonus(cargo, recebe):
    if recebe != 's':
        return 0

    if cargo == 1:
        return 1000
    elif cargo == 2:
        return 500
    elif cargo == 3:
        return 300
    elif cargo == 4:
        return 100
    else:
        return 0

nome_funcionario = input("Digite o nome do funcionário: ")
nome_cargo = int(input("Digite o cargo: (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário) "))
salario_base = float(input("Digite o salário base: R$"))
horas_extras = int(input("Digite o total de horas extras trabalhadas: "))
total_faltas = int(input("Digite o total de faltas no mês: "))
recebe_bonus = input("Recebeu bônus por desempenho? (s - Sim, n - Não) "))

print(f"Nome do funcionário: {nome_funcionario}")
print(f"Salário bruto: R$ {salario_base:.2f}")
print(f"Total de acréscimos: R$ {calcular_horas_extras(salario_base, horas_extras) + calcular_bonus(nome_cargo, recebe_bonus):.2f}")
print(f"Total de descontos: R$ {calcular_descontos_faltas(salario_base, total_faltas):.2f}")
print(f"Salário final: R$ {(salario_base + calcular_horas_extras(salario_base, horas_extras) + calcular_bonus(nome_cargo, recebe_bonus)) - calcular_descontos_faltas(salario_base, total_faltas):.2f}")
