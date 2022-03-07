'''lista2_Q4. Faça um programa que grave uma lista com 15 posições, calcule e mostre:
a) O maior elemento da lista e em que posição esse elemento se encontra;
b) O menor elemento da lista e em que posição esse elemento se encontra.'''

lista = []
maior = menor = 0
for c in range(0, 15):
    lista.append(int(input("Digite um número: ")))
    if c == 0:
        maior = menor = lista[0]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]

for i, v in enumerate(lista):
    if v == maior:
        print(f'O maior número digitado foi {maior} na posição {i+1}')
for i, v in enumerate(lista):
    if v == menor:
        print(f'O menor número digitado foi {menor} na posição {i+1}')

