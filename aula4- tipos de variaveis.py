#Todos os is:
#alfabetico - isalpha 
#numerico - isnumeric
#só tem espaços - isspace
#alfabético e numérico - isalnum
#está em maiúsculas - isupper
#está em minúculas - islower
#está só com a primeira letra em maiúsulas - istitle
a = input('Digite algo: ')
print('O tipo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabético? ', a.isalpha())
print('Está em maiúsculas? ', a.isupper())
print('Está em minúsculas? ', a.islower())
print('Está capitalizado? ', a.istitle())
