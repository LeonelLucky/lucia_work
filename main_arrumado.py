import random
posicao_certa = 0
lucia = 1
while lucia == 1:
    numero_secreto = random.randint(1000, 9999)
    n1 = numero_secreto // 1000
    n2 = (numero_secreto % 1000) // 100
    n3 = (numero_secreto % 100) // 10
    n4 = numero_secreto % 10
    
    traco1 = -1
    traco2 = -1
    traco3 = -1
    traco4 = -1

    print(" => Bem-vindo Ao Jogo SECRETO!!! <=")
    print("Você tem 10 tentativas para acertar um número entre [1000 e 9999].")
    print("A partir da 5ª tentativa, o jogo dará dicas mostrando quais dígitos estão corretos.")
    input("<<< Tecle Algo para começar >>>")
    print('-----------------------------')

    tentativa = 1
    while tentativa <= 10:
        palpite = int(input(f"Tentativa {tentativa} - Digite seu palpite: "))

        while palpite < 1000 or palpite > 9999:
            print('Entrada Inválida! Digite um número entre 1000 e 9999.')
            palpite = int(input(f"Tentativa {tentativa} - Digite seu palpite: "))

        c1 = palpite // 1000
        c2 = (palpite % 1000) // 100
        c3 = (palpite % 100) // 10
        c4 = palpite % 10
        
        if palpite == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} na {tentativa}ª tentativa!")
            break

        print("Você não acertou o código. Tente novamente!")
        dica_secreta = random.randint(1, 4)
        deu_dica = 0
        cont = 0 
        if tentativa > 3:
            print("DICAS:")
                               
        if c1 == n1:
            traco1 = n1
        if c2 == n2:
            traco2 = n2
        if c3 == n3:
            traco3 = n3
        if c4 == n4:
            traco4 = n4

        if tentativa >4:        
            if c1 != n1 and dica_secreta == dica_secreta:
            
                if n1 >= 5:
                    print("O primeiro dígito é maior ou igual a 5.")
                else: 
                    print("O primeiro dígito é menor que 5.")

                if n1 % 2 == 0:
                    print("O primeiro dígito é par.")
                else:
                    print("O primeiro dígito é ímpar.")
                    dica_secreta == dica_secreta + 1
                if c2 != n2 and dica_secreta == dica_secreta:    
            
                    if c2 != n2:
                        if n2 >= 5:
                            print("O segundo dígito é maior ou igual a 5.")
                    else:
                        print("O segundo dígito é menor que 5.")

                    if n2 % 2 == 0:
                        print("O segundo dígito é par.")
                    else:
                        print("O segundo dígito é ímpar.")
                if c3 != n3 and dica_secreta == dica_secreta:
            
                    if c3 != n3:
                        if n3 >= 5:
                            print("O terceiro dígito é maior ou igual a 5.")
                    else:
                        print("O terceiro dígito é menor que 5.")

                    if n3 % 2 == 0:
                        print("O terceiro dígito é par.")
                    else:
                        print("O terceiro dígito é ímpar.")
                    dica_secreta = dica_secreta + 1
                if c4 != n4 and dica_secreta == dica_secreta:
            
                    if c4 != n4:
                        if n4 >= 5:
                            print("O quarto dígito é maior ou igual a 5.")
                    else:
                        print("O quarto dígito é menor que 5.")

                    if n4 % 2 == 0:
                        print("O quarto dígito é par.")
                    else:
                        print("O quarto dígito é ímpar.")
                    dica_secreta = dica_secreta + 1

        print(traco1, traco2, traco3, traco4)
        print('-----------------------------')

        tentativa += 1  

    if palpite != numero_secreto:
        print(f"Você não acertou. O número secreto era {numero_secreto}.")

    lucia = int(input("Você deseja jogar novamente? (1/0) 1 = sim | 0 = nao "))
    
    while lucia != 1 and lucia != 0:
        print("Entrada inválida! Digite '1' para sim ou '0' para não.")
        lucia = int(input("Você deseja jogar novamente? (1/0): "))

print("Obrigado por jogar! Até a próxima.")
