while True:

    cpf = input('Digite o CPF que deseja verificar (11 números): ')
    tcpf = len(cpf)

    if not cpf.isnumeric() or tcpf < 11 or tcpf >= 12:
        print('Digite novamente.')
        print()
        continue

    soma_total = 0
    x = 0
    for m_1 in range(10, 1, -1):
        soma = m_1 * int(cpf[x])
        soma_total += soma
        x += 1

    conta_valid = (11 - (soma_total % 11))

    if conta_valid > 9:
        conta_valid = 0

    soma_total_1 = 0
    y = 0
    for m_2 in range(11, 2, -1):
        soma_1 = m_2 * int(cpf[y])
        soma_total_1 += soma_1
        y += 1

    soma_total_1 += (conta_valid * 2)

    conta_valid_1 = (11 - (soma_total_1 % 11))

    if conta_valid_1 > 9:
        conta_valid_1 = 0

    conta_valid = str(conta_valid)
    conta_valid_1 = str(conta_valid_1)

    cpf_novo = cpf[:9] + conta_valid + conta_valid_1

    if cpf == cpf_novo:
        print('CPF Válido.')
    else:
        print('CPF Inválido.')
    print()
