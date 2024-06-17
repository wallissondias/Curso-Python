km = float(input('Quantos km rodados? '))
dias = float(input('Quantos dias ficou alugado? '))
valor = (km * 0.15) + (dias * 60)
print(f'O total a pagar é de R${valor:.2f}')