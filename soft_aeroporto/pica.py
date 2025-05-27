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
            cidadeorigem = input('Digite o nome da cidade de origem: ').lower().strip()
            cidadedestino = input('Digite o nome da cidade de destino: ').lower().strip()
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
                    if dados['origem']== search_origem.lower().strip():
                        print(f"\nVoo {numvoo}: {dados['origem']} -> {dados['destino']} | Escalas: {dados['escalas']} | Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
                        encontrado = True
                if encontrado == False:
                    print('\nVoo não cadastrado.')
            if consultar == 3:
                encontrado = False
                search_destino=input("Insira a cidade destino que você deseja consultar:")
                for numvoo, dados in dict_Voo.items():
                    if dados['destino']== search_destino.lower().strip():
                        print(f"Voo {numvoo}: {dados['origem']} -> {dados['destino']} | Escalas: {dados['escalas']} | Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
                        encontrado = True
                if encontrado == False:
                    print('\nVoo não cadastrado.') 
                    
    if opcao == 3:
        if len(dict_Voo) == 0:
            print('\nNenhum voo cadastrado ainda!')
        else:
            menor_escala = None
            voo_menor_escala = None

            for numvoo, dados in dict_Voo.items():
                if menor_escala is None or dados['escalas'] < menor_escala:
                    menor_escala = dados['escalas']
                    voo_menor_escala = numvoo
                else:
                    print(f"\nO voo número {voo_menor_escala} tem o menor número de escalas")


    if opcao == 4:     
        if len(dict_Voo) == 0:
            print('\nNenhum voo cadastrado ainda!')
        else:         
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
                        armazem_voo[voo_desejado]= {'pessoa':[nome], 'lugares':[lugaresdisponiveis - 1 ]}
                        print("Passageiro cadastrado com sucesso.")

                    else:
                        nome = pes[cpf][0] #vai pegar o nome, usa isso pro estudo dps
                        armazem_voo[voo_desejado] = {'pessoa': [nome], 'lugares': [dict_Voo[voo_desejado]['lugares disp'] -1]}
                        dict_Voo[voo_desejado]['lugares disp'] -= 1
                        print("Passageiro cadastrado com sucesso.")
                        
                    if dict_Voo[voo_desejado]['lugares disp'] == 0:
                        voo_disp.remove(voo_desejado)
                else:
                    print("Este voo näo possui lugares disponíveis")
                print (armazem_voo)
            else:
                print("Número de voo inválido.")
                    
    if opcao == 5:
        if len(dict_Voo) == 0:
            print('\nNenhum voo cadastrado ainda!')
        else:
            print ("\nVoos Registrados")
            for numvoo, dados in dict_Voo.items():
                print(f"Voo {numvoo}: {dados['origem']} para {dados['destino']} | Escalas: {dados['escalas']} | " f"Preço: R${dados['preço']:8.2f} | Lugares: {dados['lugares disp']}")
                print ("-"*80)
                
            ver_voo= int(input("Digite o voo que deseja consultar: "))
            
            if ver_voo in armazem_voo.keys():
                for num_voo, voo_dados in armazem_voo.items():
                    print (f'Voo numero {ver_voo}, possui como passageiros as pessoas {voo_dados['pessoa']}, e possui {voo_dados['lugares']} lugares disponíveis')
                
            while ver_voo not in armazem_voo:
                print("\nPor favor, digite um voo registrado")
                ver_voo=int(input("Digite o voo que deseja consultar: "))
            
    if opcao == 6 : 
       if len(dict_Voo) == 0:
            print('\nNenhum voo cadastrado ainda!')
       else:
           cpf_cancel= (input('Digite seu cpf: ')).strip()
           if cpf_cancel in armazem_voo:
               nome_passageiro = pes[cpf_cancel][0]
               print(armazem_voo)
               voo_cancel=int(input('Digite o voo que você deseja cancelar: '))
               if voo_cancel in armazem_voo.keys() and nome_passageiro in armazem_voo[voo_cancel]:
                   armazem_voo[voo_cancel].remove(nome_passageiro)
                   armazem_voo[voo_cancel][lugaresdisponiveis] +=1 
                   dict_Voo[voo_cancel]['lugares disp'] += 1
                   print(f'O voo de número {voo_cancel}, teve o passageiro de nome {nome_passageiro} removido')
               while voo_cancel not in armazem_voo:
                   print("\nDigite um voo válido")
                   voo_cancel=int(input('Digite o voo que você deseja cancelar: '))

    if opcao == 7:
        print('\n')
        print('-' *34)
        print('Obrigado por usar nossos serviços')
        print('-' *34)
        menu=0
