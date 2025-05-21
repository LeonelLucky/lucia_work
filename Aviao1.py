dVoo = {}
cdVoo = {}
csVoo = {}

menu = 1
while menu == 1:
    print('----------------MENU----------------')
    print('1. Cadastrar voo')
    print('2. Consultar voo')
    print('3. Sair')
    escolha = input('Digite sua opção: ')

    if escolha == '1':
        voos = int(input('\nDeseja cadastrar quantos voos? '))
        
        for i in range(voos):
            numVoo = int(input('\nDigite o numero do voo: '))
            cidadeorigem = input('Digite o nome da cidade de origem: ')
            cidadedestino = input('Digite o nome da cidade de destino: ')
            numescalas = int(input('Digite o numero de escalas: '))
            preçopassagem = float(input('Digite o preço da passagem: '))
            lugaresdisponiveis = int(input('Digite a quantidade de lugares disponiveis: '))

            cdVoo[numVoo] = {
                'Origem': cidadeorigem,
                'Destino': cidadedestino,
                'Escalas': numescalas,
                'Preço da Passagem': preçopassagem,
                'Lugares Disponiveis': lugaresdisponiveis
            }
            print(f'\nVoo {numVoo} cadastrado com sucesso!')
            print(cdVoo[numVoo])

    elif escolha == '2':
        if cdVoo == None:
            print('\nNenhum voo cadastrado ainda!')
        else:
            consultar = int(input('\nDigite o numero do voo: '))
            if consultar in cdVoo:
                print('\nInformações do voo:')
                print(cdVoo[consultar])
            else:
                print('\nVoo não cadastrado.')
    
    elif escolha == '3':
        print('\nSaindo do sistema...')
        break
    
    else:
        print('\nOpção inválida! Digite 1, 2 ou 3.')
