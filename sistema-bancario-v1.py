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
    
    opcao = int(input(menu))
    
    if opcao == 1:
        deposito = float(input("Qual valor deseja depositar? "))
        if deposito > 0:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            
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
        
        else: 
            print(f"Valor invalido. Tente novamente. \n\n")
    
    elif opcao == 3:
        print("\n================== EXTRATO ====================")
        print("Não foram realizadas moviemntações." if not extrato else extrato)
        print(f"\nSALDO: R$ {saldo:.2f}")
        
        
    elif opcao == 4:
        break     
    
    else:
        print("Opção invalida. Tente novamente.")
        
print("Obrigado por usar nosso banco!")