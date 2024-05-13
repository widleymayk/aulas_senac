'''
contador_de_n_impares = [1, 2, 3, 4, 5, 6]
for a in input(int):
    nova_lista = [1 , 3, 5] 
    for b in a:
       nova_lista.append(b.split(1 , 5))
    contador_de_n_impares.append(nova_lista)
a = contador_de_n_impares
print(contador_de_n_impares)
'''
'''
def contador_de_n_impares (soma)
x = 1
lista = [1, 2, 3, 4, 5]
print('Digite 20 números.')
while x <= 20:
    n = int(input('Digite um número: [ %s ]: '%x))
    lista.append(n)
    x += 1
print('O maior valor é:',max(lista))
print(contador_de_n_impares)
'''
numeros = input ("digite uma lista de numeros separados por espaco").split()
numeros = [int(numero) for numero in numeros]
z = 0
for numero in numeros:
    if numero % 2 != 0:
        z = z+1
print(z)