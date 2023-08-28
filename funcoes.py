import pytest

# Código da função para o Exercício 01
def calcular_salario_liquido(valor_hora_aula, numero_aulas, percentual_inss):
    salario_bruto = valor_hora_aula * numero_aulas
    desconto_inss = salario_bruto * (percentual_inss / 100)
    salario_liquido = salario_bruto - desconto_inss
    return salario_liquido

#--------------------------------------------------

# Código da função para o Exercício 02
def aplicar_desconto(valor_produto):
    desconto = valor_produto * 0.09
    novo_valor = valor_produto - desconto
    return novo_valor, desconto


#--------------------------------------------------

# Código da função para o Exercício 03
def calcular_valor_promocao(valor_original, desconto):
    valor_promocao = valor_original - desconto
    return valor_promocao

#--------------------------------------------------

# Código da função para o Exercício 04
def calcular_conta_restaurante(despesa):
    gorjeta = despesa * 0.10
    total_conta = despesa + gorjeta
    return total_conta, gorjeta


