nome = str(input('Digite seu nome completo: '))
print(f'Seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome tem ao todo {len(nome)} letras')
divide = nome.split()
print(f'Seu primeiro nome é {divide[0]} e ele tem {len(divide[0])} letras')
