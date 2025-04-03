import random 
numero_secreto = random.randint(1000, 9999)  
n1= numero_secreto//1000
n2= (numero_secreto%1000)//100
n3= (numero_secreto%100)//10
n4= (numero_secreto%10)
<<<<<<< HEAD
tentativas=0
traco1= ("_")
traco2= ("_")
traco3= ("_")
traco4= ("_")
=======
traco1= str ("_")
traco2= str ("_")
traco3= str ("_")
traco4= str ("_")
print (n1)
print (n2)
print (n3)
print (n4)
>>>>>>> 4be354a2faefc03b096ce5e6880ab0987ea4b98c
print(" => Bem-vindo Ao Jogo SECRETO!!! <=")
print("Você tem 10 tentativas para acertar um numero entre [1000 e 9999].")
print("A partir da 5a tentativas, o jogo irá te ajudar, dando dicas.")
input("<<< Tecle Algo >>>")
print('-----------------------------')

<<<<<<< HEAD
while tentativas<10:
    palpite = int(input("Digite seu palpite: "))  
    c1 = palpite//1000
    c2 = (palpite%1000)//100
    c3 = (palpite%100)//10
    c4 = (palpite%10)
    while (c1==0) or (palpite>9999):
        print (f"O valor digitado não é válido, digite novamente")
        palpite = int(input("Digite seu palpite novamente: "))
        break

    tentativas+=1
    if palpite == numero_secreto: 
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} na {tentativas} tentativa!")
        break
    print (f"Tentativa {tentativas} Você digitou {palpite}. Tente novamente!")
    
    if tentativas >= 5:
        print("Dica: Você acertou alguns números!")

    if tentativas > 0:
            
        if c1 == n1:
            traco1 = n1
        if c2 == n2:
            traco2 = n2
        if c3 == n3:
            traco3 = n3
        if c4 == n4:
            traco4 = n4
    print (f"{traco1} {traco2} {traco3} {traco4}")
    
    print(f"Comparando: ({c1}, {c2}, {c3}, {c4}) == ({n1}, {n2}, {n3}, {n4})")
else:
    print(f"Você não acertou o número. O número secreto era {numero_secreto}")
             
print("Fim do jogo!")  
jogar_denovo= input("Gostaria de jogar novamente ? (s/n)")

if jogar_denovo== ("s"):
    
    import random 
    numero_secreto = random.randint(1000, 9999)  
    while tentativas<10:
        
        palpite = int(input("Digite seu palpite: "))  
        c1 = palpite//1000
        c2 = (palpite%1000)//100
        c3 = (palpite%100)//10
        c4 = (palpite%10)
        
        while (c1==0) or (palpite>9999):
            print (f"O valor digitado não é válido, digite novamente")
            palpite = int(input("Digite seu palpite novamente: "))
            break 
        
        tentativas+=1
        if palpite == numero_secreto: 
            print(f"Parabéns! Você acertou o número secreto {numero_secreto} na {tentativas} tentativa!")
            break
        print (f"Tentativa {tentativas} Você digitou {palpite}. Tente novamente!")
    
        if tentativas >= 5:
            print("Dica: Você acertou alguns números!")

        if tentativas > 0:
            
            if c1 == n1:
                traco1 = n1
            if c2 == n2:
                traco2 = n2
            if c3 == n3:
                traco3 = n3
            if c4 == n4:
                traco4 = n4
        print(f"Comparando: ({c1}, {c2}, {c3}, {c4}) == ({n1}, {n2}, {n3}, {n4})")
    else:
        print(f"Você não acertou o número. O número secreto era {numero_secreto}")
else:
    print("Fim do jogo!")
=======
palpite = int(input("Digite seu palpite: "))  
c1 = palpite//1000
c2 = (palpite%1000)//100
c3 = (palpite%100)//10
c4 = (palpite%10)
print (c1)
print (c2)
print (c3)
print (c4)
if palpite == numero_secreto:
    print(f"Parabéns! Você acertou o número secreto {numero_secreto} na 1ª tentativa!")
else:
    for i in range(10):
        print(f"Tentativa {i+1} Você digitou {palpite}. Tente novamente!")
        
        palpite = int(input("Digite seu palpite: "))
        if (c1==n1):
            traco1=n1
            print (f"{traco1} {traco2} {traco3} {traco4}")
        elif (c2==n2):
            traco2=n2
            print (f"{traco1} {traco2} {traco3} {traco4}")
        elif (c3==n3):
            traco3=n3
            print (f"{traco1} {traco2} {traco3} {traco4}")
        elif (c4==n4):
            traco4=n4
            print (f"{traco1} {traco2} {traco3} {traco4}")
        else:
            print ("_ _ _ _")
    else:
        print("Você não acertou nenhum número")
print("Fim do jogo!")   
