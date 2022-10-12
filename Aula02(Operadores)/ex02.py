# Crie um programa que leia um valor em metros e o exiba convertido na tabela de medidas,.

m = int(input('>>> DIGITE UMA MEDIDA EM METROS [m]: \n> '))
Km = m / 1000
Hm = m / 100
Dam = m / 10
#m = equivale ao que o usuário digitar!
dm = m * 10
cm = m * 100
mm = m * 1000
print(f'''  TABELA DE CONVERSÃO:
- Km:  {Km}Km
- Hm:  {Hm}Hm
- Dam: {Dam}Dam
- m:   {m}m
- dm:  {dm}dm
- cm:  {cm}cm
- mm:  {mm}mm''')