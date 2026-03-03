# ============================================================
# ATIVIDADE 04
# Autor: Davi Alexandre Nunes
# Data: 03/03/2026
# Linguagem: Python
#
# ------------------------------------------------------------
# OBJETIVO:
# Desenvolver um programa que receba três valores inteiros
# (X, Y e Z) informados pelo usuário e verifique se esses
# valores podem formar os lados de um triângulo. Caso formem,
# o programa deve informar se o triângulo é equilátero,
# isósceles ou escaleno.
#
# ------------------------------------------------------------
# DESCRIÇÃO:
# Para que três valores formem um triângulo, é necessário
# obedecer à condição de existência do triângulo:
# - Cada lado deve ser menor que a soma dos outros dois.
#
# Classificação dos triângulos:
# - Equilátero: todos os lados iguais.
# - Isósceles: dois lados iguais.
# - Escaleno: todos os lados diferentes.
#
# ============================================================


# -------------------------------
# ENTRADA DE DADOS
# -------------------------------
# Solicita ao usuário os três valores inteiros
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))
z = int(input("Digite o valor de Z: "))


# -------------------------------
# PROCESSAMENTO
# -------------------------------
# Verifica se os valores podem formar um triângulo
# A condição abaixo garante que cada lado é menor
# que a soma dos outros dois
if (x < y + z) and (y < x + z) and (z < x + y):

    # Se formar um triângulo, verifica o tipo
    if x == y and y == z:
        tipo = "equilátero"
    elif x == y or x == z or y == z:
        tipo = "isósceles"
    else:
        tipo = "escaleno"

    resultado = "Os valores formam um triângulo " + tipo
else:
    resultado = "Os valores informados NÃO formam um triângulo"


# -------------------------------
# SAÍDA DE DADOS
# -------------------------------
# Exibe o resultado final para o usuário
print(resultado)