# Desafio Sistema Bancario
Esta é uma solução pro desafio de codigo do bootcamp da DIO, no curso de python.

## Problema
Criar um sistema bancário com três funcões básicas: **Deposito**, **Saque**, **Extrato**.

1. **Deposito**
  - Deve ser possivel depositar valores positivos
  - Deve ser armazenadas em uma variavel
  - Deve ser exibido na operação de extrato
2. **Saque**
  - Deve ser possivel sacar apenas 3 vezes ao dia
  - Deve ser possivel sacar ni maximo R$ 500.00
  - Deve ser mostrado uma mensagem caso usuario tenha saldo insuficiente
  - Deve ser armazenados em uma variavel
  - Deve ser exibido na operação de extrato
3. **Extrato**
  - Deve ser exibidos os depositos e saques realizados
  - Deve ser exibido o saldo atual no final
  - Deve ser exibido no formato: R$ XXX.XX
  ```python
  > 1500 = R$ 1500.00
  ```

## Template
Esse template foi disponibilizado pelo professor da aula

```python
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


while True:
    opcao = input(menu)
    if opcao == "d":
        print("Depósito")
    elif opcao == "s":
        print("Saque")
    elif opcao == "e":
        print("Extrato")
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada")
```

> NOTA: lembrado que não precisa seguir o padrão do template ou a lógica, o que importa são as funcionalidades que foram pedidas
