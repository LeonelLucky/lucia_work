dict_Voo = {}
pes= {}
armazem_voo= {}
menu = 1
while menu == 1:
    
    print('----------------MENU----------------')
    print("\n Escolha uma opção")
    print("1. Cadastrar voos")
    print("2. Consultar voos")
    print("3. Voo com menor escala")
    print("4. Comprar Passagem")
    print("5. Passageiros voo")
    print("6.Cancelar passagem")
    print("7. Sair")
    opcao = int(input('\nDigite o numero da opção: '))

    if opcao == 1:
        voos = int(input('\nDeseja cadastrar quantos voos? '))
    
        for i in range(voos):
            
            numVoo = int(input('Digite o numero do voo: '))
            cidadeorigem = input('Digite o nome da cidade de origem: ')
            cidadedestino = input('Digite o nome da cidade de destino: ')
            numescalas = int(input('Digite o numero de escalas: '))
            preçopassagem = float(input('Digite o preço da passagem: '))
            lugaresdisponiveis = int(input('Digite a quantidade de lugares disponiveis: '))

            dict_Voo[numVoo] =  {'origem': cidadeorigem,'destino': cidadedestino,'escalas': numescalas,'preço': preçopassagem,'lugares disp': lugaresdisponiveis}
            for numvoo, dados in dict_Voo.items():
                print(f"Voo {numvoo}: {dados['origem']} para {dados['destino']} | Escalas: {dados['escalas']} | " f"Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
                print ("-"*80)
                print (dict_Voo.keys())   

    if opcao == (2):
        if dict_Voo == None:
            print('\nNenhum voo cadastrado ainda!')
        else:
            consultar = int(input('\nDigite o numero do voo ou a cidade origem ou a cidade destino: '))
            if consultar in dict_Voo.keys():
                for numvoo, dados in dict_Voo.items():
                    print(f"Voo {numvoo}: {dados['origem']} para {dados['destino']} | Escalas: {dados['escalas']} | " f"Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
            else:
                print('\nVoo não cadastrado.')
    
    if opcao == 3:
        menor_escala = numescalas
        if numescalas > menor_escala:
            menor_escala = numescalas
            print (f"O voo com a menor escala se trata do voo número {dict_Voo[numVoo][menor_escala]}")

    if opcao == 4:
        
        if dict_Voo == None:
            print('\nNenhum voo cadastrado ainda!')
        if dict_Voo['lugares disp'] >= 0:
            print('Sem voos com lugares disponiveis')
        else:
            print ("\nVoos Disponíveis")
            print(f"Voo {numvoo}: {dados['origem']} para {dados['destino']} | Escalas: {dados['escalas']} | " f"Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
            print ("-"*80)

            voo_desejado= int(input("\nDigite o numero do voo desejado:"))       
            if voo_desejado in dict_Voo.keys():
                cpf = input("Digite seu CPF: ")
                if cpf not in pes.keys(): 
                    nome = input("Nome do passageiro: ")
                    telefone = input("Telefone do passageiro: ")
                    pes[cpf] = [nome, telefone]
                    armazem_voo[voo_desejado]= {'pessoa':[nome], 'lugares':[lugaresdisponiveis-1]}
                    print("Passageiro cadastrado com sucesso.")
                    print(pes)
                    print(armazem_voo)
                else:
                    cpf = armazem_voo[voo_desejado].update(armazem_voo)
                    print(armazem_voo)
                    dict_Voo[voo_desejado][lugaresdisponiveis]=-1
        if opcao == 5:
            if dict_Voo == None:
                print('\nNenhum voo cadastrado ainda!')
            else:
                pas_voo= int(input("Digite o numero do voo desejado: "))

                
                    print(armazem_voo)
                else:
                    cpf = armazem_voo[voo_desejado].update(armazem_voo)
                    print(armazem_voo)
