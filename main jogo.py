import random

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
input("<<< Tecle Algo >>>")
print('-----------------------------')

tentativa = 1
while tentativa <= 10:
    palpite = int(input(f"Tentativa {tentativa} - Digite seu palpite: "))
    if palpite < 1000 or palpite > 9999:
        print('Entrada Invalida!')
        tentativa -= 1
    
    c1 = palpite // 1000
    c2 = (palpite % 1000) // 100
    c3 = (palpite % 100) // 10
    c4 = palpite % 10
    
    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} na {tentativa}ª tentativa!")
        break
    
    print(f"Você digitou {palpite}. Tente novamente!")
    
    if tentativa > 0:
        if c1 == n1:
            traco1 = n1
        if c2 == n2:
            traco2 = n2
        if c3 == n3:
            traco3 = n3
        if c4 == n4:
            traco4 = n4
        print(traco1, traco2, traco3, traco4)
    
    tentativa += 1  
if palpite != numero_secreto:
    print(f"Você não acertou. O número secreto era {numero_secreto}.")
if tentativa > 10 or palpite == numero_secreto:
    print("Fim do jogo!")

    



