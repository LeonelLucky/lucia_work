
# tela de inicio

print('Bem-Vindo ao Jogo SECRETO!!!')

print('Você tem 10 tentativas para acertar o número secreto entre 1000 e 9999')

print('A partir da 5a. tentativa o jogo irá te ajudar, dando dicas.')
input('Tecle algo ')
print('--------------------------------------------')

#tentativa(mexi nos c's e n's)
tentativa = int(input('Seu código é: '))
c1 = tentativa//1000
c2 = (tentativa%1000)//100
c3 = (tentativa%100)//10
c4 = (tentativa%10)
n1= 2006//1000
n2= (2006%1000)//100
n3= (2006%100)//10
n4= (2006%10)

if (2006) == tentativa:
    print('PARABENS VOCÊ ACERTOU!!!')
else:
    for i in range (10):
        if c1= n1:
        print (f"{{c1} _ _ _")
        elif c2=n2:
    
    print('VOCÊ NÃO ACERTOU NADA NESSA TENTATIVA ...')

            print('PARABENS VOCÊ ACERTOU!!!')