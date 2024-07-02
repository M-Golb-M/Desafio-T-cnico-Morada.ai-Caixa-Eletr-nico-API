print('=' * 30)
print('{:^30}'.format('Banco Cuphead'))
print('=' * 30)

# LOGIN DO USUARIO
cpf = ''
senha = ''
while (cpf != '12345678900' or senha != '12345'):
    cpf = input('Digite seu CPF: ')
    senha = input('Digite sua senha: ')

    if (cpf != '12345678900' or senha != '12345'):
        print("Dados incorretos!")

# SISTEMA DO BANCO
saldo = 100
opcao = 0

while (opcao != 4):
    # Menu do banco
    print('=' * 30)
    print("Digite a opção desejada: ")
    print("1 - Saldo")
    print("2 - Saque")
    print("3 - Depósito")
    print("4 - Sair")
    print('=' * 30)
    opcao = int(input('Opção: '))

    if opcao == 1:
        # Saldo
        print(f"Seu saldo é de: R${saldo}")

    elif opcao == 2:
        # Saque
        valor = int(input("Quanto deseja sacar? "))
        if valor <= saldo:
            saldo -= valor
            print(f"Você sacou R${valor}. Seu novo saldo é R${saldo}.")
        else:
            print("Saldo insuficiente!")

    elif opcao == 3:
        # Depósito
        valor = int(input("Quanto deseja depositar? "))
        saldo += valor
        print(f"Você depositou R${valor}. Seu novo saldo é R${saldo}.")

    elif opcao == 4:
        print("Obrigado por usar o Banco Cuphead! Volte sempre.")
    else:
        print("Opção inválida! Tente novamente.")