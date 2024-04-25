menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

-> """

balance = 0
limit = 500
extract = ""
number_withdrawals = 0
LIMIT_WITHDRAWALS = 3


while True:
    option = input(menu)

    if option == "1":
        print("Depósito")
        deposit_value = float(input("Valor a ser depositado: "))

        if deposit_value > 0:
            balance += deposit_value
            extract += f"Deposito realizado: +R$ {deposit_value:.2f}\n"
            print(f"R$ {deposit_value:.2f} Depositados")

    elif option == "2":
        print("Saque")
        withdraw_value = float(input("Valor a ser sacado: "))

        if number_withdrawals < LIMIT_WITHDRAWALS:
            if withdraw_value <= 500.00 and withdraw_value <= balance:
                balance -= withdraw_value
                number_withdrawals += 1
                extract += f"Saque realizado: -R$ {withdraw_value:.2f}\n"
                print(f"R$ {withdraw_value:.2f} sacados")
            else:
                print("Saldo insuficiente ou limite de saque atingido")
        else:
            print("Voce nao pode mais realizar saque hoje, volte amanha")

    elif option == "3":
        print("Extrato")
        print(extract)
        print(f"Saldo total: R$ {balance:.2f}")

    elif option == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
