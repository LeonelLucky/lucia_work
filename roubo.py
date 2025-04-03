import random
lucia = 's'
while lucia == 's':
    numero_secreto = random.randint(1000, 9999)
    n1 = numero_secreto // 1000
    n2 = (numero_secreto % 1000) // 100
    n3 = (numero_secreto % 100) // 10
    n4 = numero_secreto % 10
    print(numero_secreto)

    traco1 = "_"
    traco2 = "_"
    traco3 = "_"
    traco4 = "_"

    print(" => Bem-vindo Ao Jogo SECRETO!!! <=")
    print("Você tem 10 tentativas para acertar um número entre [1000 e 9999].")
    print("A partir da 5ª tentativa, o jogo dará dicas mostrando quais dígitos estão corretos.")
    input("<<< Tecle Algo >>>")
    print('-----------------------------')

    tentativa = 1
    while tentativa <= 10:
        
        palpite = int(input(f"Tentativa {tentativa} - Digite seu palpite: "))
        c1 = palpite // 1000
        c2 = (palpite % 1000) // 100
        c3 = (palpite % 100) // 10
        c4 = palpite % 10
        
        certo1=0
        certo2=0
        certo3=0
        certo4=0
        
        if palpite < 1000 or palpite > 9999:
            print('Entrada Invalida!')
            tentativa -= 1
        
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto:.0f} na {tentativa}ª tentativa!")
            break
        
        print(f"Você não acertou o código. Tente novamente!")
        
        if tentativa >= 5:
            if (n1 >= 5) and (c1 >= 5) and (c1!=n1):
                print('O primeiro digito é maior que ou igual a 5')
            else: 
                print('O primeiro digito é menor que 5') 
        
            if (n2 >= 5)and (c2 >= 5) and (c2!=n2):
                print('O segundo digito é maior ou igual a 5')
            else: 
                print('O segundo digito é menor que 5')   
                
            if (n3 >= 5) and (c3 >= 5) and (c3!=n3):
                print('O terceiro digito é maior ou igual a 5')
            else: 
                print('O terceiro digito é menor que 5')   

            if (n4 >= 5) and (n4 >= 5) and (c4!=n4):
                print('O quarto digito é maior ou igual a 5')
            else: 
                print('O quarto digito é menor que 5')   
            if (n1 % 2 == 0)and(c1 % 2== 0) and (c1!=n1):
                print('O primeiro digito é par')
            else: 
                print('O primeiro digito é impar')    
            
            if (n2  % 2 == 0) and (c2 % 2 == 0) and (c2!=n2):
                print('O segundo digito é par')
            else: 
                print('O segundo digito é impar') 
        
            if (n3 % 2  == 0) and (c3 % 2 ==0 ) and (c3!=n3):
                print('O terceiro digito é par')
            else: 
                print('O terceiro digito é impar')

            if (n4 and c4 % 2==0) and (c4!=n4):
                print('O quarto digito é par')
            else: 
                print('O quarto digito é impar')
        
        if tentativa > 0:
            if c1 == n1:
                traco1 = n1
                certo1=1
            if c2 == n2:
                traco2 = n2
                certo2=1
            if c3 == n3:
                traco3 = n3
                certo3=1
            if c4 == n4:
                traco4 = n4
                certo4=1
            print(traco1, traco2, traco3, traco4)
        
        tentativa += 1  
        
    if palpite != numero_secreto:
        print(f"Você não acertou. O número secreto era {numero_secreto}.")
        
    if certo1 == 1 and certo2 == 1 and certo3 == 1 and certo4 == 1:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto:.0f} na {tentativa}ª tentativa!")
        break
        
    if tentativa > 10 or palpite == numero_secreto:
        print("Fim do jogo!")
        
    lucia=(input("Voce deseja jogar denovo ?(s/n)"))
    
    if lucia != ('s') and lucia!= ('n'):
        print ("A entrada digitada é invalida, porfavor digite (s/n)")
        lucia=(input("Voce deseja jogar denovo ?(s/n)"))