'''Lista2_Q5. Faça um programa que leia duas listas de 10 elementos numéricos cada um e intercale os
elementos deste em uma outra lista de 20 elementos.'''

lista1 = []
lista2 = []

cont = 0

for i in range(20):
    n = int(input('Digite um número: '))
    cont +=1
    if cont <= 10:
        lista1.append(n)
    else:
        lista2.append(n)


lista3 =[]
for i in range(10):
    lista3.append(lista1[i])
    lista3.append(lista2[i])

print(f'A lista 1 {lista1[:]}')
print(f'Lista 2 {lista2[:]}')
print(f'Lista 3 {lista3}')

