'''lista2_Q3. Faça um programa que dada uma seqüência de n números, imprimi-la na ordem inversa à da
leitura.'''


rodada = int(input('Digite quantas vezes o programa vai pedir o número: '))
n = []
while rodada > 0:
    n.append(int(input('Digite um número: ')))
    rodada-=1
    n.sort(reverse=True)
print(n)