from textwrap import dedent


def menu():
    menu = """
        ############################
                                
            Selecione uma opção: 

            1 - Criar Conta
            2 - Criar cliente
            3 - Depositar
            4 - Sacar
            5 - Exibir extrato
            6 - Sair

        ############################
    """
    return int(input(menu))

def depositar(saldo, valor, extrato,/): 
    if valor > 0:
        saldo += valor
        extrato += f"Deposito R$ {valor:.2f}"
        print(f"Depositado R$ {valor:.2f} com sucesso!")
    
    else: 
        print("Valor invalido. Tente novamente")
        main()
    
    return saldo, extrato
    main()
        
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if sacar > saldo: 
        print("Saldo insuficiente. Tente novamente.") 
        main()
    
    elif numero_saques >= limite_saques:
        print("Limite de saques atingido. Tente novamente amanhã")
    
    elif valor > limite: 
        print("O valor que deseja sacar ultrapassa o seu limite de saque. Tente novamente.")
        main()
    
    else: 
        saldo -= valor
        extrato += f"Saque R$ {valor:2f}" 
        
    return saldo, extrato
    main()
    
def exibir_extrato(saldo, /, *, extrato):
    print("\n================== EXTRATO ====================")
    print("Não foram realizadas moviemntações." if not extrato else extrato)
    print(f"\n\nSALDO: R$ {saldo:.2f}")
    main()
            
def criar_usuario(usuarios):
    cpf = input("Informe seu CPF(somente numeros):\n")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario:
        print("Usuario já existe com esse CPF!")
        return
                
    nome = input("Informe o seu nome:\n")
    data_nascimento = input("Informe sua data de nascimento(01/01/2001):")
    endereco = input("Informe seu endereço (logradour, numero - bairro - cidade/sigla estado): \n")
    
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereço" : endereco})
    
    print("Usuario criado com sucesso!")
    main()
    
def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def cria_conta(agencia, numero_conta, usuarios):
    cpf = input("Qual o CPF do usuario:\n")
    usuario = filtrar_usuarios(cpf, usuarios)
    
    if usuario: 
        print("Conta criada com sucesso!")
        return{"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("Usuario não cadastrado, gentileza realizar criação!")
    main()

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
       
    saldo = 0
    limite_por_saque = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    
    opcao = menu()
    
    while True: 
    
        if opcao == 3: 
            deposito = float(input("Qual valor deseja depositar?\nR$ "))
            
            saldo, extrato = depositar(saldo, deposito, extrato)
        
        elif opcao == 4:
            saque = float(input("Qual valor deseja sacar:\nR$ "))
            
            saldo, extrato = sacar(saldo= saldo, valor= saque, extrato= extrato, limite= limite_por_saque, numero_saques= numero_saques, limite_saques= LIMITE_SAQUES)

        elif opcao == 5:
            exibir_extrato(saldo, extrato = extrato)
        
        elif opcao == 6: 
            break
        
        elif opcao == 1:
            print("Recebeu")
            numero_conta = len(contas) + 1
            conta = cria_conta(AGENCIA, numero_conta, usuarios) 
            
            if conta: 
                contas.append(conta)
        
        elif opcao == 2:
            criar_usuario(usuarios)
                      
main()