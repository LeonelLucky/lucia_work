
dict_Voo = {}
pes= {}
armazem_voos= []
armazem_passageiros= []

menu = 1
while menu == 1:
    
    print('----------------MENU----------------')
    cadastrar_voos = input('Deseja cadastrar voos? Aperte 1!')
    if cadastrar_voos == '1':
        voos = int(input('\nDeseja cadastrar quantos voos? '))
    
        for i in range(voos):
            
            numVoo = int(input('Digite o numero do voo: '))
            cidadeorigem = input('Digite o nome da cidade de origem: ')
            cidadedestino = input('Digite o nome da cidade de destino: ')
            numescalas = int(input('Digite o numero de escalas: '))
            preçopassagem = float(input('Digite o preço da passagem: '))
            lugaresdisponiveis = int(input('Digite a quantidade de lugares disponiveis: '))

            dict_Voo[numVoo] =  {'origem': cidadeorigem,'destino': cidadedestino,'escalas': numescalas,'preço': preçopassagem,'lugares disp': lugaresdisponiveis}
            armazem_voos.append(numVoo)
            for numvoo, dados in dict_Voo.items():
                print(f"Voo {numvoo}: {dados['origem']} para {dados['destino']} | Escalas: {dados['escalas']} | " f"Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
                           
def cadastrar_passageiro():
    cpf = input("Digite seu CPF: ")
    if cpf in pes.keys():
        print(f"\n\t\t=> CPF JÁ EXISTENTE<==\n")
    else:
        nome = input("Nome do passageiro: ")
        telefone = input("Telefone do passageiro: ")
        pes[cpf] = [nome, telefone]
        armazem_passageiros.append(cpf)
        print("Passageiro cadastrado com sucesso.")
        print(pes)
            
cadastrar_passageiro()



    