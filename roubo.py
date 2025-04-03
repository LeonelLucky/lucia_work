import random 
numero_secreto = random.randint(1000, 9999)  
n1= numero_secreto//1000
n2= (numero_secreto%1000)//100
n3= (numero_secreto%100)//10
n4= (numero_secreto%10)

tentativas=0
traco1= ("_")
traco2= ("_")
traco3= ("_")
traco4= ("_")
print (n1)
print (n2)
print (n3)
print (n4)

print(" => Bem-vindo Ao Jogo SECRETO!!! <=")
print("Você tem 10 tentativas para acertar um numero entre [1000 e 9999].")
print("A partir da 5a tentativas, o jogo irá te ajudar, dando dicas.")
input("<<< Tecle Algo >>>")
print('-----------------------------')

while tentativas<10:
    palpite = int(input("Digite seu palpite: "))  
    c1 = palpite//1000
    c2 = (palpite%1000)//100
    c3 = (palpite%100)//10
    c4 = (palpite%10)
    while (c1==0) or (palpite>9999):
        print (f"O valor digitado não é válido, digite novamente")
        tentativas-=1

    tentativas+=1
    if palpite == numero_secreto: 
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} na {tentativas} tentativa!")
        break
    print (f"Tentativa {tentativas} Você digitou {palpite}. Tente novamente!")
    
    if tentativas >= 5:
        
            if n1 >= 5:
                print('O primeiro digito é maior que ou igual a 5')
            else: 
                print('O primeiro digito é menor que 5') 
        
            if n2 >= 5:
                print('A segundo digito é maior ou igual a 5')
            else: 
                print('A segundo digito é menor que 5')   

            if n3 >= 5:
                print('A terceiro digito é maior ou igual a 5')
            else: 
                print('A terceiro digito é menor que 5')   

            if n4 >= 5:
                print('A quarto digito é maior ou igual a 5')
            else: 
                print('A quarto digito é menor que 5')   

            if n1 % 2 == 0:
                print('O primeiro digito é par')
            else: 
                print('O primeiro digito é impar')    
            
            if n2 % 2 == 0:
                print('O segundo digito é par')
            else: 
                print('O segundo digito é impar') 

            if n3 % 2 == 0:
                print('O terceiro digito é par')
            else: 
                print('O terceiro digito é impar')

            if n4 % 2 == 0:
                print('O quarto digito é par')
            else: 
                print('O quarto digito é impar') 

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
