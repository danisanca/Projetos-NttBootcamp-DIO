boas_vindas = """

#### Bem Vindo

"""
menu = """

#### Selecione uma opção

[d] Depositar
[s] Sacar
[e] Extrato

[q] Sair

=>"""

saldo =0
limite_diario=500
extrato=""
numero_saques=0
LIMITE_SAQUES =3

print(boas_vindas)
while True:
    opcao=input(menu)
    if opcao == "d":
        valor = float(input("Informe o valor do deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é invalido")
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        limite_saldo = valor > saldo
        limite_diario = valor > limite_diario
        limite_saque = numero_saques >= LIMITE_SAQUES
        if limite_saldo:
            print("Operação falhou! Voce não tem saldo suficiente.")
        elif limite_diario:
            print("Operação falhou! O valor do saque excede o limite.")
        elif limite_saque:
            print("Operação falhou! Número maximo de saques excedido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques +=1
        else:
            print("Operação falhou! O valor informado é invalido")
    elif opcao == "e":
        print("\n ============== EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print(" ============== EXTRATO ==============")
    elif opcao == "q":
        break
    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")
