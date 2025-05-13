cdVoo = {}  # Dicionário de voos
pes = {}    # Dicionário de passageiros
armazem_voos = []          # Lista de voos cadastrados
armazem_passageiros = []   # Lista de passageiros cadastrados

def cadastrar_voos():
    voos = int(input('\nDeseja cadastrar quantos voos? '))
    for i in range(voos):
        numVoo = int(input('\nDigite o número do voo: '))
        cidadeorigem = input('Digite a cidade de origem: ')
        cidadedestino = input('Digite a cidade de destino: ')
        numescalas = int(input('Digite o número de escalas: '))
        preco = float(input('Digite o preço da passagem: '))
        lugares = int(input('Digite a quantidade de lugares disponíveis: '))

        cdVoo[numVoo] = {
            "origem": cidadeorigem,
            "destino": cidadedestino,
            "escalas": numescalas,
            "preco": preco,
            "lugares": lugares
        }

        armazem_voos.append(numVoo)
        print(f"Voo {numVoo} cadastrado com sucesso!")

def cadastrar_passageiro():
    cpf = input("\nDigite o CPF do passageiro: ")
    if cpf in pes:
        print("⚠️ CPF já cadastrado!")
    else:
        nome = input("Digite o nome do passageiro: ")
        telefone = input("Digite o telefone do passageiro: ")
        pes[cpf] = {"nome": nome, "telefone": telefone}
        armazem_passageiros.append(cpf)
        print("Passageiro cadastrado com sucesso!")

def listar_voos():
    if not cdVoo:
        print("Nenhum voo cadastrado ainda.")
        return
    print("\n--- Voos Cadastrados ---")
    for num, dados in cdVoo.items():
        print(f"Voo {num}: {dados['origem']} -> {dados['destino']} | Escalas: {dados['escalas']} | "
              f"Preço: R${dados['preco']} | Lugares: {dados['lugares']}")

def menu():
    while True:
        print("\n========= MENU =========")
        print("1. Cadastrar voos")
        print("2. Cadastrar passageiro")
        print("3. Listar voos")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_voos()
        elif opcao == "2":
            cadastrar_passageiro()
        elif opcao == "3":
            listar_voos()
        elif opcao == "4":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Executa o menu principal
menu()
