import random

from click import clear 
cont = 0
acertos = 0
acerto = list()
turma = ['Maria', 'João', 'Sergio', 'Carlos', 'Manoel']
gabarito = ['A', 'B', 'C', 'D', 'E','A', 'B', 'C', 'D', 'E','A', 'B', 'C', 'D', 'E','A', 'B', 'C', 'D', 'E','A', 'B', 'C', 'D', 'E','A', 'B', 'C', 'D', 'E']
cartao_resposta = ['A', 'B', 'C', 'D', 'E']


print('======================= Gabarito =========================================')

for i in range(30):
    cont+=1
    print(f'Questão {cont} {gabarito[i]}')




#Maria
cont = 0
print(f'====================================== {turma[0]} =====================================')
for i in range(30):
    cartao_resposta = random.choice(gabarito)
    cont+=1
    print(f'{turma[0]}  {cont}:{cartao_resposta}.')
    if cartao_resposta == gabarito[i]:
     acertos+=1
     acerto.append(cont)
     if acertos > 15:
         print('Parabéns {turma[0]} você acertou mais da metade da prova!')

print(f'.................{turma[0]} teve {acertos} acertos.')
print(f'acertou as questões {acerto}')


#João
print(f'====================================== {turma[1]} =====================================')
cont = 0
acertos = 0
acerto = list()
for i in range(30):
    cartao_resposta = random.choice(gabarito)
    cont+=1
    print(f'{turma[1]}  {cont}:{cartao_resposta}.')
    if cartao_resposta == gabarito[i]:
     acertos+=1
     acerto.append(cont)
     if acertos > 15:
         print('Parabéns {turma[1]} você acertou mais da metade da prova!')
print(f'........................{turma[1]} teve {acertos} acertos.')
print(f'Você acertou as questões: {acerto}')


print(f'====================================== {turma[2]} =====================================')
cont = 0
acertos = 0
acerto = list()
for i in range(30):
    cartao_resposta = random.choice(gabarito)
    cont+=1
    print(f'{turma[2]}  {cont}:{cartao_resposta}.')
    if cartao_resposta == gabarito[i]:
     acertos+=1
     acerto.append(cont)
     if acertos > 15:
         print('Parabéns {turma[2]} você acertou mais da metade da prova!')
print(f'........................{turma[2]} teve {acertos} acertos.')
print(f'Você acertou as questões: {acerto}')



print(f'====================================== {turma[3]} =====================================')
cont = 0
acertos = 0
acerto = list()
for i in range(30):
    cartao_resposta = random.choice(gabarito)
    cont+=1
    print(f'{turma[3]}  {cont}:{cartao_resposta}.')
    if cartao_resposta == gabarito[i]:
     acertos+=1
     acerto.append(cont)
     if acertos > 15:
         print('Parabéns {turma[3]} você acertou mais da metade da prova!')
print(f'........................{turma[3]} teve {acertos} acertos.')
print(f'Você acertou as questões: {acerto}')

print(f'====================================== {turma[4]} =====================================')
cont = 0
acertos = 0
acerto = list()
for i in range(30):
    cartao_resposta = random.choice(gabarito)
    cont+=1
    print(f'{turma[4]}  {cont}:{cartao_resposta}.')
    if cartao_resposta == gabarito[i]:
     acertos+=1
     acerto.append(cont)
     if acertos > 15:
         print('Parabéns {turma[4]} você acertou mais da metade da prova!')
print(f'........................{turma[4]} teve {acertos} acertos.')
print(f'Você acertou as questões: {acerto}')





 
 