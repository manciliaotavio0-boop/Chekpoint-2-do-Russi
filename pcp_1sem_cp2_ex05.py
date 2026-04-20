nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))
renda = float(input('Digite sua renda mensal: '))
vl_emprestimo = float(input('Digite o valor do empréstimo: '))

qtd_parcela = 0

while qtd_parcela < 3 or qtd_parcela > 24:
    qtd_parcela = int(input('Digite a quantidade de parcelas que deseja (3 - 24): '))

def pode_aprovar(idade, renda, vl_emprestimo):
    if idade < 18:
        return False
    if vl_emprestimo > (renda * 20):
        return False
    return True

def definir_taxa(qtd_parcela):
    if qtd_parcela <= 6:
        return 0.05
    elif qtd_parcela <= 12:
        return 0.08
    else:
        return 0.10

def calc_parcela(vl_emprestimo, taxa, qtd_parcela):
    parcela = vl_emprestimo * (taxa * (1 + taxa) ** qtd_parcela) / ((1 + taxa) ** qtd_parcela - 1)
    return parcela

def calc_total(vl_emprestimo, qtd_parcela):
    total = vl_emprestimo * qtd_parcela
    return total

def calc_juros(total, vl_emprestimo):
    juros = total - vl_emprestimo
    return juros

if pode_aprovar(idade, renda, vl_emprestimo):
    taxa = definir_taxa(qtd_parcela)
    parcela = calc_parcela(vl_emprestimo, taxa, qtd_parcela)
    total = calc_total(parcela, qtd_parcela)
    juros = calc_juros(total, vl_emprestimo)

    print(f'''Empréstimo aprovado
          
    Nome do cliente: {nome}
    Valor financiado: R$ {vl_emprestimo:.2f}
    Taxa de juros: {taxa * 100:.0f}% ao mês
    Valor da parcela: R$ {parcela:.2f}
    Valor total pago: R$ {total:.2f}
    Total de juros pagos: R$ {juros:.2f}
    ''')
else:
    print('Empréstimo reprovado')