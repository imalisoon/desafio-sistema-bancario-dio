# Desafio Sistema Bancario
Esta é uma melhoria da primeira solução do desadio de código do bootcamp da DIO, no curso de python.

- [Primeira solução](../)

## Problema
Melhorar a primeira solução separando as funções existentes (depósito, saque, extrato) seguindo algumas regras, e criar 2 novas funções (criar usuario, criar conta).

1. **Depósito** (Positional only)
    - sug. argumentos: saldo, valor, extrato
    - sug, retorno: saldo, extrato
2. **Saque** (keyword only)
    - sug. argumentos: saldo, valor, extrato etc.
    - sug. retorno: saldo, extrato
3. **Extrato** (Positional only & Keyword only)
    - positional: saldo
    - keyword: extrato
4. **Usuários**
    - deve ser armazenados em uma **lista**
    - deve ter:
        - nome
        - data de nascimento (dd-mm-aaaa)
        - cpf (numeros sem pontos/traços)
        - endereço (logradouro, nro - bairro - cidade/sigla estado)
    - deve ser possivel apenas 1 usuario com mesmo **CPF**
5. **Contas**
    - deve ser armazenadas em uma **lista**
    - deve ter:
        - agência (fixo "0001")
        - numero da conta (sequencial iniando  1)
        - usuário
    - usuario pode ter mais de uma conta
    - uma conta so pode está associada a um usuário

> NOTA: Novas funções são bem vindas, como por exemplo, listar contas, listar usuarios ou verificar_usuario.
