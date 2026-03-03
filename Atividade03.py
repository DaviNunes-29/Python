# ============================================================
# ATIVIDADE 03
# Autor: Davi Alexandre Nunes
# Data: 03/03/2026
# Linguagem: Python
#
# ------------------------------------------------------------
# OBJETIVO:
# Desenvolver um programa que leia um número inteiro informado
# pelo usuário e determine se esse número é par ou ímpar.
#
# ------------------------------------------------------------
# DESCRIÇÃO:
# Um número é considerado par quando o resto da sua divisão por
# 2 é igual a zero. Caso contrário, o número é considerado ímpar.
# Para essa verificação, o programa utiliza o operador de resto
# da divisão (%), juntamente com uma estrutura condicional
# (if / else).
#
# ============================================================


# -------------------------------
# ENTRADA DE DADOS
# -------------------------------
# Solicita ao usuário que digite um número inteiro
# input() lê o valor digitado
# int() converte o valor digitado (texto) para número inteiro
numero= int(input("Informe seu número inteiro:"))


# -------------------------------
# PROCESSAMENTO
# -------------------------------
# Verifica se o número é par ou ímpar
# Se o resto da divisão por 2 for igual a 0, o número é par
if numero % 2 == 0:
    resultado = "par"
else:
    resultado = "ímpar"


# -------------------------------
# SAÍDA DE DADOS
# -------------------------------
# Exibe o resultado da verificação para o usuário
print("O número digitado é", resultado)