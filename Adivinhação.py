import random 
print('-'*80)
print('\n') #usados apenas para fins de estética do código

print('Vamos jogar um jogo de advinhação, te desafio a ganhar de mim.\n') #primeira notificação do usuário
def adivinhacao():
    lista =[0, 1, 2, 3, 4, 5]
    numpc1 = random.choice(lista)
    numuser = int(input('Digite seu número da sorte de 0 a 5, e vamos ver se vai vencer: ')) # Entrada de dados
    if numuser == numpc1:
        print(f'O nomero escolhido pelo pc foi: {numpc1}') # Saída de dados
        print('Parabéns, você venceu\n'.upper())
        print(' ')
        print('-'*80) # Usado apenas para fins de estética do código
    else:
        print(f'O nomero escolhido pelo pc foi: {numpc1}')
        print(f'Não foi desta vez, tente novamente \n')
        adivinhacao()
adivinhacao()
print('-'*80) # Usado apenas para fins de estética do código
