import random  # o random é uma biblioteca de aleatórios (random)

numero_secreto = random.randint(1000, 9999)  # o comando random.randint gera um numero aleatorio, esse 1000 e 9999 é que nem o range que a gente usa no for, começo e final só que 9999 faz parte do comando, assim como 1000
tentativas = 0  

print(" => Bem-vindo Ao Jogo SECRETO!!! <=")
print("Você tem 10 tentativas para acertar um numero entre [1000 e 9999].")
print("A partir da 5a tentativas, o jogo irá te ajudar, dando dicas.")
input("<<< Tecle Algo >>>")
print('-----------------------------')

while tentativas < 10:
    palpite = input("Digite seu palpite: ")  # primeiro palpite

    # pra garantir que o usuario digite numeros inteiros ao inves de float e caracteres usei o palpite.isdigit() e pro usuario digitar 4 numeros usei o len(palpite), que conta os caracteres da variavel e se for diferente de 4 ele vai pedir a impressao correta
    while not palpite.isdigit() or len(palpite) != 4:
        print("Entrada inválida! Digite um número de 4 dígitos.")
        palpite = input("Digite seu palpite: ")

    palpite = int(palpite)  
    tentativas += 1  

    if palpite == numero_secreto:
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas!")
        break
    else:
        print(f"Tentativa {tentativas}/10: Você digitou {palpite}. Tente novamente!")

print("Fim do jogo!")  