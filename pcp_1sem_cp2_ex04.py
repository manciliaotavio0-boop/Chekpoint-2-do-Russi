nome_func = input("Digite o nome do funcionário: ")
cargo = int(input("Digite o cargo: (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário) "))
salario_base = float(input("Digite o salário base: R$"))
hora_extra = int(input("Digite o total de horas extras trabalhadas: "))
falta = int(input("Digite o total de faltas no mês: "))
bonus = int(input("Recebeu bônus por desempenho? (1-Sim, 2-Não) "))

def calcular_horas_extras(salario, total_horas):
    horas_extras = (salario * 0.015) * total_horas + salario
    return horas_extras

def calcular_descontos_faltas(a, b):
    descontos_falta = (a * 0.02) * b
    return descontos_falta

def calcular_bonus(cargoo):
    if cargoo == 1:
        valor_bonus = 1000
    elif cargoo == 2:
        valor_bonus = 500
    elif cargoo == 3:
        valor_bonus = 300
    elif cargoo == 4:
        valor_bonus = 100
    else:
        valor_bonus = 0

salario_extra = calcular_horas_extras(salario_base, hora_extra)

desconto_falta = calcular_descontos_faltas(salario_base, falta)