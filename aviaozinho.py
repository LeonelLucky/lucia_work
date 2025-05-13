dVoo = {}
cdVoo = {}
csVoo = {}



menu = 1
while menu == 1:
    
    print('----------------MENU----------------')
    cadastrar_voos = input('Deseja cadastrar voos? Aperte 1!')
    if cadastrar_voos == '1':
        voos = int(input('\nDeseja cadastrar quantos voos? '))
    
        for i in range(voos):
            numVoo = int(input('Digite o numero do voo: '))
            cidadeorigem = input('Digite o nome da cidade de origem: ')
            cidadedestino = input('Digite o nome da cidade de destino')
            numescalas = int(input('Digite o numero de escalas'))
            preçopassagem = float(input('Digite o preço da passagem: '))
            lugaresdisponiveis = int(input('Digite a quantidade de lugares disponiveis: '))

            cdVoo[numVoo] = {
            'Origem': cidadeorigem,
            'Destino': cidadedestino,
            'Escalas': numescalas,
            'Preço da Passagem': preçopassagem,
            'Lugares Disponiveis': lugaresdisponiveis
            }
            print(cdVoo)
    
    if cadastrar_voos != '1':
        print('Entrada inválida! Digite 1 caso queria cadastrar um ou mais voos.')
    
        





