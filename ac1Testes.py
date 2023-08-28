import pytest
from funcoes import calcular_salario_liquido
from funcoes import aplicar_desconto
from funcoes import calcular_valor_promocao
from funcoes import calcular_conta_restaurante


# Conjunto de testes para o Exercício 01

def test_calcular_salario_liquido():
    assert calcular_salario_liquido(6.25, 160, 1.3) == 987.00
    assert calcular_salario_liquido(20.5, 240, 1.7) == 4836.36
    assert calcular_salario_liquido(13.9, 200, 6.48) == 2599.86

# Conjunto de testes para o Exercício 02

def test_aplicar_desconto():
    assert aplicar_desconto(100) == (91.00, 9.00)
    assert aplicar_desconto(1500) == (1365.00, 135.00)
    assert aplicar_desconto(60000) == (54600.00, 5400.00)

# Conjunto de testes para o Exercício 03

def test_calcular_valor_promocao():
    assert calcular_valor_promocao(500.00, 50.00) == 450.00
    assert calcular_valor_promocao(10500.00, 500.00) == 10000.00
    assert calcular_valor_promocao(90.00, 0.80) == 89.20

# Conjunto de testes para o Exercício 04

def test_calcular_conta_restaurante():
    assert calcular_conta_restaurante(75.00) == (82.50, 7.50)
    assert calcular_conta_restaurante(125.00) == (137.50, 12.50)
    assert calcular_conta_restaurante(350.87) == (385.96, 35.09)