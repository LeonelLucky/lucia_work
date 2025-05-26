dict_Voo = {}
pes= {}
armazem_voo= {}
voo_disp = []
    
menu = 1

while menu == 1:
    
    print('\n----------------MENU----------------')
    print("\n Escolha uma opção")
    print("1. Cadastrar voos")
    print("2. Consultar voos")
    print("3. Voo com menor escala")
    print("4. Comprar Passagem")
    print("5. Passageiros voo")
    print("6. Cancelar passagem")
    print("7. Sair")
    opcao = int(input('\nDigite o numero da opção: '))

    if opcao == 1:
        voos = int(input('\nDeseja cadastrar quantos voos? '))
    
        for i in range(voos):
            numVoo = int(input('\nDigite o numero do voo: '))
            while numVoo in dict_Voo:
                print(f"O voo {numVoo} já está cadastrado. Digite outro número de voo. ")
                numVoo=int(input("\nAperte enter para digitar o numero do voo novamente: "))
            cidadeorigem = input('Digite o nome da cidade de origem: ')
            cidadedestino = input('Digite o nome da cidade de destino: ')
            numescalas = int(input('Digite o numero de escalas: '))
            preçopassagem = float(input('Digite o preço da passagem: '))
            lugaresdisponiveis = int(input('Digite a quantidade de lugares disponiveis: '))
            print('-'*80)
            
                    
            dict_Voo[numVoo] =  {'origem': cidadeorigem,'destino': cidadedestino,'escalas': numescalas,'preço': preçopassagem,'lugares disp': lugaresdisponiveis}
            voo_disp.append(numVoo)
            print (dict_Voo)
               
    if opcao == 2:
        if len(dict_Voo) == 0:
            print('\nNenhum voo cadastrado ainda!')
        else:
            print("\nConsultar pelo número do voo (1).\nConsultar pela cidade origem (2).\nConsultar pela cidade destino (3)")
            consultar = int(input('Digite a opção de consulta: '))
            
            if consultar == 1:
                search_voo= int(input("Insira o número do Voo que você deseja consultar:"))
                if search_voo in dict_Voo.keys():
                    dados_voo = dict_Voo[search_voo]
                    print (f"\nVoo {search_voo}: {dados_voo['origem']} para {dados_voo['destino']} | Escalas: {dados_voo['escalas']} | Preço: R${dados_voo['preço']:8.2f} | Lugares: {dados_voo['lugares disp']}")
                else:
                    print('\nVoo não cadastrado.')
            if consultar == 2:
                search_origem= input("Insira a cidade de origem que você deseja consultar:")
                encontrado = False
                for numvoo, dados in dict_Voo.items():
                    if dados['origem'].lower().strip() == search_origem.lower().strip():
                        print(f"\nVoo {numvoo}: {dados['origem']} -> {dados['destino']} | Escalas: {dados['escalas']} | Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
                        encontrado = True
                if encontrado == False:
                    print('\nVoo não cadastrado.')
            if consultar == 3:
                encontrado = False
                search_destino=input("Insira a cidade destino que você deseja consultar:")
                for numvoo, dados in dict_Voo.items():
                    if dados['destino'].lower().strip() == search_destino.lower().strip():
                        print(f"Voo {numvoo}: {dados['origem']} -> {dados['destino']} | Escalas: {dados['escalas']} | Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
                        encontrado = True
                if encontrado == False:
                    print('\nVoo não cadastrado.') 
    if opcao == 3:
        if len(dict_Voo) == 0:
            print('\nNenhum voo cadastrado ainda!')
        else:
            menor_escala = None
            for numvoo, dados in dict_Voo.items():
                if dados['escalas'] < menor_escala:
                    menor_escala = dados['escalas']
                    print(f'O voo número {menor_escala} possui menos voo')

    if opcao == 4:                    
            print ("\nVoos Disponíveis")
            print (voo_disp)
            for numvoo, dados in dict_Voo.items():
                print(f"Voo {numvoo}: {dados['origem']} para {dados['destino']} | Escalas: {dados['escalas']} | " f"Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
                print ("-"*80)

            voo_desejado= int(input("\nDigite o numero do voo desejado:"))  
                 
            if voo_desejado in dict_Voo.keys():
                if voo_desejado in voo_disp:
                    cpf = input("Digite seu CPF: ")
                
                    
                    if cpf not in pes.keys(): 
                        nome = input("Nome do passageiro: ")
                        telefone = input("Telefone do passageiro: ")
                        pes[cpf] = [nome, telefone]
                        
                        dict_Voo[voo_desejado]['lugares disp'] -= 1
                        armazem_voo[voo_desejado]= {'pessoa':[nome], 'lugares':[lugaresdisponiveis-1]}
                        print("Passageiro cadastrado com sucesso.")
                        
                    if dict_Voo[voo_desejado]['lugares disp'] == 0:
                        voo_disp.remove(voo_desejado)
                    else:
                        nome = pes[cpf][0]
                        armazem_voo[voo_desejado] = {'pessoa': [nome], 'lugares': [dict_Voo[voo_desejado]['lugares disp'] - 1]}
                        dict_Voo[voo_desejado]['lugares disp'] -= 1
                        print("Passageiro cadastrado com sucesso.")
                else:
                    print("Este voo näo possui lugares disponíveis")
                    
    if opcao == 5:
        print ("\nVoos Registrados")
        for numvoo, dados in dict_Voo.items():
            print(f"Voo {numvoo}: {dados['origem']} para {dados['destino']} | Escalas: {dados['escalas']} | " f"Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
            print ("-"*80)
            
        ver_voo= (input("Digite o voo que deseja consultar: "))
        
        if ver_voo in armazem_voo:
            for num_voo, voo_dados in armazem_voo:
                print (f'Voo numero {ver_voo}, possui como passageiros as pessoas {voo_dados['pessoa']}, e possui {voo_dados['lugares']} disponíveis')
            
        while ver_voo not in armazem_voo:
            print("\nPor favor, digite um voo registrado")
            ver_voo=input("Digite o voo que deseja consultar: ")
            
    if opcao == 6 : 
        voo_cancel= print ('Digite o voo que voce deseja cancelar a passagem: ')
        
