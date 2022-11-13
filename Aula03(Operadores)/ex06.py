# Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
#   --> formula:  F = (9 * C + 160) / 5
titulo = 'CONVERSOR DE TEMPERATURAS'
print(f'\033[4;31m{titulo:-^50}\033[m')
tempC = float(input('Digite uma temperatura em graus Celsius(°C):'))
tempF = (9 * tempC + 160) / 5
print('-'*50)
print(f'Temperatura: \033[33m{tempC}°C\033[m  --> \033[32m{tempF}°F\033[m')
