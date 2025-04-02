import random  # o random é uma biblioteca de aleatórios (random)

numero_secreto = random.randint(1000, 9999)  # o comando random.randint gera um numero aleatorio, esse 1000 e 9999 é que nem o range que a gente usa no for, começo e final só que 9999 faz parte do comando, assim como 1000
tentativas = 0  
c1 = palpite//1000
c2 = (palpite%1000)//100
c3 = (palpite%100)//10
c4 = (palpite%10)
n1= numero_secreto//1000
n2= (numero_secreto%1000)//100
n3= (numero_secreto%100)//10
n4= (numero_secreto%10)
traco1= str ("_")
traco2= str ("_")
traco3= str ("_")
traco4= str ("_")

print(" => Bem-vindo Ao Jogo SECRETO!!! <=")
print("Você tem 10 tentativas para acertar um numero entre [1000 e 9999].")
print("A partir da 5a tentativas, o jogo irá te ajudar, dando dicas.")
input("<<< Tecle Algo >>>")
print('-----------------------------')


while tentativas < 10:
    palpite = int(input("Digite seu palpite: "))  # primeiro palpite  
    tentativas += 1 
    if palpite == numero_secreto:
         print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
    else:
        if (c1==n1):
            traco1=c1 
            print (f"{traco1} {traco2} {traco3} {traco4}")
        elif (c2==n2):
            traco2=c2
            print (f"{traco1} {traco2} {traco3} {traco4}")
        elif (c3==n3):
            traco3=c3
            print (f"{traco1} {traco2} {traco3} {traco4}")
        elif (c4==n4):
            traco4=c4
            print (f"{traco1} {traco2} {traco3} {traco4}")
        else:
            print ("_ _ _ _")
            

        print(f"Tentativa {tentativas}/10: Você digitou {palpite}. Tente novamente!")

print("Fim do jogo!")  
c1 = palpite//1000
c2 = (palpite%1000)//100
c3 = (palpite%100)//10
c4 = (palpite%10)
n1= numero_secreto//1000
n2= (numero_secreto%1000)//100
n3= (numero_secreto%100)//10
n4= (numero_secreto%10)
traco1= str ("_")
traco2= str ("_")
traco3= str ("_")
traco4= str ("_")
for i in range (10):
    if palpite == numero_secreto:
         print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
    else:
        if (c1==n1):
            traco1=c1 
            print (f"{traco1} {traco2} {traco3} {traco4}")
        elif (c2==n2):
            traco2=c2
            print (f"{traco1} {traco2} {traco3} {traco4}")
        elif (c3==n3):
            traco3=c3
            print (f"{traco1} {traco2} {traco3} {traco4}")
        elif (c4==n4):
            traco4=c4
            print (f"{traco1} {traco2} {traco3} {traco4}")
        else:
            print ("_ _ _ _")
            

        print(f"Tentativa {tentativas}/10: Você digitou {palpite}. Tente novamente!")

print("Fim do jogo!")  