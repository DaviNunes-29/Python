# ============================================================
# ATIVIDADE 01
# Autor: Davi Alexandre Nunes
# Data: 03/03/2026
# Linguagem: Python
#
# ------------------------------------------------------------
# OBJETIVO:
# Fazer um programa para receber um número inteiro de segundos do usuário e
# imprimir a quantidade correspondente em horas, minutos e segundos.
#
# ------------------------------------------------------------
# DESCRIÇÃO:
# Para realizar a conversão, o programa utiliza operações de
# divisão inteira e resto da divisão.
# Sabemos que:
# - 1 hora equivale a 3600 segundos
# - 1 minuto equivale a 60 segundos
#
# Primeiro, são calculadas as horas inteiras contidas no total
# de segundos. Em seguida, calcula-se o restante de segundos
# para determinar os minutos e, por fim, os segundos finais.
#
# ============================================================

# Primeiro, pedimos ao usuário que informe a quantidade de segundos
segundos = int(input("Digite a quantidade de segundos: "))

# Calculamos as horas inteiras
# // = divisões inteiras, descarta casas decimais
horas = segundos // 3600

# Calculamos o restante de segundos após retirar as horas
# % = resto da divisão
resto = segundos % 3600

# Calculamos os minutos inteiros a partir do restante
minutos = resto // 60

# O que sobra são os segundos finais
segundos_finais = resto % 60

# Exibimos o resultado
print("Horas:", horas)
print("Minutos:", minutos)
print("Segundos:", segundos_finais)