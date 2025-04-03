c1 = int(2)
c2 = int(0)
c3 = int(0)
c4 = int(6)
n1= str("_")
n2= str("_")
n3= str("_")
n4= str("_")
# tela de inicio

print('Bem-Vindo ao Jogo SECRETO!!!')

print('Você tem 10 tentativas para acertar o número secreto entre 1000 e 9999')

print('A partir da 5a. tentativa o jogo irá te ajudar, dando dicas.')
input('Tecle algo ')
print('--------------------------------------------')

tentativa = int(input('Seu código é: '))

if (2006) == tentativa:
    print('PARABENS VOCÊ ACERTOU!!!')
else:
    print('VOCÊ NÃO ACERTOU NADA NESSA TENTATIVA ...')
    for i in range(10):
        tentativa = int(input(f'{i + 1}ª tentativa'))
        print (f'Seu código é {n1} {n2} {n3} {n4}')
        
        if c1==2:
            n1=c1
        if c2==0:
            n2=c2
        if c3==0:
            n3=c3
        if c4==6:
            n4=c4
        if (c1) and (c2) and (c3) and (c4) == tentativa:
            print('PARABENS VOCÊ ACERTOU!!!')

    