valor = float(input('Uma distancia em metros: '))
km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000
print(f'A medida {valor} é:')
print(f'A medida em km é {km}')
print(f'A medida em hm é {hm}')
print(f'A medida em dam é {dam}')
print(f'A medida em dm é {dm}')
print(f'A medida em cm é {cm}')
print(f'A medida em mm é {mm}')