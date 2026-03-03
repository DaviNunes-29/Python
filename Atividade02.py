# ============================================================
# ATIVIDADE 02
# Autor: Davi Alexandre Nunes
# Data: 03/03/2026
# Linguagem: Python
#
# ------------------------------------------------------------
# OBJETIVO:
# Fazer um programa para receber 3 valores inteiros do usuário e mostrar a sua
# média (que pode não ser inteira).
#
# ------------------------------------------------------------
# DESCRIÇÃO:
# A média aritmética é obtida somando todos os valores e
# dividindo o resultado pela quantidade de valores.
# Neste programa, serão solicitados três números inteiros,
# que serão somados e divididos por 3, gerando a média.
#
# ============================================================


# -------------------------------
# ENTRADA DE DADOS
# -------------------------------
# Aqui o programa solicita ao usuário o primeiro número inteiro
# A função input() lê o valor digitado
# A função int() converte o valor digitado (texto) para número inteiro
nota1 = float(input("DIGITE SUA PRIMEIRA NOTA: "))
nota2 = float(input("DIGITE SUA SEGUNDA NOTA: "))
nota3 = float(input("DIGITE SUA TERCEIRA NOTA: "))


# -------------------------------
# PROCESSAMENTO
# -------------------------------
# Nesta etapa, o programa soma os três valores informados
# Em seguida, divide o resultado por 3
# O operador / realiza divisão normal, podendo gerar um número decimal
media = (nota1 + nota2 + nota3) / 3


# -------------------------------
# SAÍDA DE DADOS
# -------------------------------
# Exibe na tela o valor da média calculada
print("Sua média é: ", media)