dict_Voo = {}
pes= {}
armazem_voos= []
armazem_passageiros= []

menu = 1
while menu == 1:
    
    print('----------------MENU----------------')
    print("\n Escolha uma opção")
    print("1. Cadastrar voos")
    print("2. Cadastrar passageiro")
    print("3. Consultar voos")
    print("4. Alterar voos")
    print("5. Sair")
    opcao = int(input('Digite o numero da opção: '))



    if opcao == (1):
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
                print ("-"*80)
                           
    if opcao == (2):
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
    
    if opcao == 3:
        search_voo = int(input("\nDigite o número do voo desejado: "))
        if search_voo in dict_Voo.keys():
                dados_voo = dict_Voo[search_voo]
                print(f"Voo {search_voo}: {dados_voo['origem']} para {dados_voo['destino']} | Escalas: {dados_voo['escalas']} | Preço: R${dados_voo['preço']:8.2f} | Lugares: {dados_voo['lugares disp']}")
        else:
            print(f"\n{search_voo} não consta no banco de dados")

    
