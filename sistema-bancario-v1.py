LIMITE_SAQUE = 3
limite = 500
saldo = 0
extrato = ""
numero_de_saques = 0
menu = f"""
############################
                         
    Selecione uma opção: 

    1 - Depositar
    2 - Sacar
    3 - Exibir extrato
    4 - Sair
    
############################
"""

while True:
    if opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
    
        if opcao == 1:
            deposito = float(input("Qual valor deseja depositar? "))
            if deposito > 0:
                saldo += deposito
                extrato += f"Deposito: R$ {deposito:.2f}\n"
                
                realizar_nova_acao = int(input("Deseja realizar novo deposito?\n1 - Sim\n2 - Não"))
                if realizar_nova_acao == 1: opcao = 1
                
            else: 
                print(f"Valor a ser depositado é invalido. Tente novamente. \n\n")
                
        elif opcao == 2: 
            sacar = float(input("Qual valor deseja sacar: "))
            
            if saldo < sacar:
                print("Saldo insuficiente para saque. \n\n")
                
            elif sacar > 500: 
                print(f"Limite de saque excedito. Seu limite de saque é de R$ {limite:.2f} \n\n")

            elif numero_de_saques == LIMITE_SAQUE:
                print("O seu limte diario de saques foi alcançado. Volte amanhã. \n\n")
                
            elif sacar > 0: 
                saldo -= sacar
                numero_de_saques += 1
                extrato += f"Saque: R$ {sacar:.2f}\n"
                
                realizar_nova_acao = int(input("Deseja realizar novo saque?\n1 - Sim\n2 - Não"))
                if realizar_nova_acao == 1: opcao = 2
            
            else: 
                print(f"Valor invalido. Tente novamente. \n\n")
        
        elif opcao == 3:
            print("\n================== EXTRATO ====================")
            print("Não foram realizadas moviemntações." if not extrato else extrato)
            print(f"\nSALDO: R$ {saldo:.2f}")
            
            realizar_nova_acao = int(input("Deseja realizar mais algum procedimento?\n1 - Sim\n 2 - Não"))
            if realizar_nova_acao == 2:  break
            
        elif opcao == 4:
            break     
        
        else:
            print("Opção invalida. Tente novamente.")

    else:
        opcao = int(input(menu))
        if opcao == 1:
            deposito = float(input("Qual valor deseja depositar? "))
            if deposito > 0:
                saldo += deposito
                extrato += f"Deposito: R$ {deposito:.2f}\n"
                
                realizar_nova_acao = int(input("Deseja realizar novo deposito?\n1 - Sim\n2 - Não"))
                if realizar_nova_acao == 1: opcao = 1
                
            else: 
                print(f"Valor a ser depositado é invalido. Tente novamente. \n\n")
                
        elif opcao == 2: 
            sacar = float(input("Qual valor deseja sacar: "))
            
            if saldo < sacar:
                print("Saldo insuficiente para saque. \n\n")
                
            elif sacar > 500: 
                print(f"Limite de saque excedito. Seu limite de saque é de R$ {limite:.2f} \n\n")

            elif numero_de_saques == LIMITE_SAQUE:
                print("O seu limte diario de saques foi alcançado. Volte amanhã. \n\n")
                
            elif sacar > 0: 
                saldo -= sacar
                numero_de_saques += 1
                extrato += f"Saque: R$ {sacar:.2f}\n"
                
                realizar_nova_acao = int(input("Deseja realizar novo saque?\n1 - Sim\n2 - Não"))
                if realizar_nova_acao == 1: opcao = 2
            
            else: 
                print(f"Valor invalido. Tente novamente. \n\n")
        
        elif opcao == 3:
            print("\n================== EXTRATO ====================")
            print("Não foram realizadas moviemntações." if not extrato else extrato)
            print(f"\nSALDO: R$ {saldo:.2f}")
            
            realizar_nova_acao = int(input("Deseja realizar mais algum procedimento?\n1 - Sim\n 2 - Não"))
            if realizar_nova_acao == 2:  break
            
        elif opcao == 4:
            break     
        
        
print("Obrigado por usar nosso banco!")