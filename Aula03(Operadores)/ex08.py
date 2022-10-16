# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a 
# quantidade de tinta necessária para pintá-la, 
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

print('Digite as informações a seguir:')
l = float(input('> Largura da parede: '))
a = float(input('> Altura da parede: '))
area_parede = l * a
quant_tinta = area_parede / 2
print(f'''> ÁREA DA PAREDE: {area_parede:.2f}m²
> LITROS DE TINTA: {quant_tinta:.2f}L''')
