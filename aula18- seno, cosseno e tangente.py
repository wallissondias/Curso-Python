from math import sin, cos, tan, radians
valor = float(input('Digite o ângulo que você deseja: '))
print(f'O ângulo de {valor} tem o SENO de {sin(radians(valor)):.2f}')
print(f'O ângulo de {valor} tem o COSSENO de {cos(radians(valor)):.2f}')
print(f'O ângulo de {valor} tem a TANGENTE de {tan(radians(valor)):.2f}')