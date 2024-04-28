AGENCY = "0001"
LIMIT_WITHDRAWALS = 3

balance = 0
limit = 500
extract = ""
number_withdrawals = 0

users = []
accounts = []
number = 1



def menu():
    print("[1] Depositar\n[2] Sacar\n[3] Extrato\n[4] Novo usuario\n[5] Listar usuarios\n[6] Criar cinta\n[7] Listar contas\n[0] Sair")

def deposit(balance, deposit_value, extract, /):
    if deposit_value <= 0:
        print("Operação cancelada, valor de depósito inválido")

    else:
        balance += deposit_value
        extract += f"Deposito realizado: +++R$ {deposit_value:.2f}\n"
        print(f"R$ {deposit_value:.2f} Depositado\n")

    return balance, extract

def withdraw(*, balance, withdraw_value, number_withdrawals, extract):
    balance -= withdraw_value
    number_withdrawals += 1
    extract += f"Saque realizado: ---R$ {withdraw_value:.2f}\n"
    print(f"R$ {withdraw_value:.2f} Retirado\n")

    return balance, number_withdrawals, extract

def get_extract(balance, /, *, extract):
    print(extract)
    print(f"Saldo em conta: R$ {balance:.2f}")

def create_user(users):
    name = input("Nome: ")
    cpf = input("CPF (numeros): ")

    birthday = input("Data de nascimento (dd-mm-aa): ")
    address = input("Endereço (log, n - bairro - cidade/sigla): ")
    if get_user(users, cpf):
        user = {
            "name": name,
            "cpf": cpf,
            "address": address
        }

        print(f"Usúario {name} criado")
        users.append(user)

    else:
        print("Usuario ja cadasyrado com esse CPF")

    return users

def get_users(users):
    print("-"*10)
    for user in users:
        print(f"Usuario: {user['name']}")
        print(f"CPF: {user['cpf']}")
        print(f"Endereco: {user['address']}")
        print("-"*10)

def get_user(users, cpf):
    for user in users:
        if user["cpf"] == cpf:
            return user

def create_account(accounts, number, users):
    cpf = input("Informe CPF: ")
    user = get_user(users, cpf)

    if user:
        account = {
            "number": number,
            "agency": agency,
            "user": user
        }
        accounts.append(account)
        print(f"Conta {number} criada")
        number += 1

    else:
        print("Nenhum usuario cadasyradovcom esse CPF")

    return accounts, number

def get_accounts(accouts):
    print("-"*10)
    for account in accounts:
        print(f"Numero: {account['number']}")
        print(f"Agencia: {account['agency']}")
        print(f"Usuario: {account['user']['name']}")
        print("-"*10)


while True:
    menu()
    option = input("-> ")

    if option == "1":
        print("\n=== DEPÓSITO ===")
        deposit_value = float(input("Valor a ser depositado: "))

        balance, extract = deposit(balance, deposit_value, extract)

    elif option == "2":
        print("\n=== SAQUE ===")
        withdraw_value = float(input("Valor a ser sacado: "))

        if withdraw_value <= 0:
            print("Operação cancelada, valor de saque inválido")
            continue
        if withdraw_value > balance:
            print("Operação cancelada, valor de saque acima do saldo")
            continue
        if withdraw_value > limit:
            print("Operação cancelada, valor de saque acima do limite")
            continue
        if number_withdrawals >= LIMIT_WITHDRAWALS:
            print("Operação cancelada, limite de saques atingido")
            continue

        
        balance, number_withdrawals, extract = withdraw(
            balance = balance, 
            withdraw_value = withdraw_value,
            number_withdrawals = number_withdrawals,
            extract = extract
        )

    elif option == "3":
        print("=== Extrato ===")
        get_extract(balance, extract=extract)

    elif option == "4":
        print("=== Novo Usuario ===")
        users = create_user(users)

    elif option == "5":
        get_users(users)

    elif option == "6":
        accounts, number = create_account(
            accounts, number, users
        )

    elif option == "7":
        get_accounts(accounts)

    elif option == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
