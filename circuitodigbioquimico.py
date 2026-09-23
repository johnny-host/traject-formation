while True:
    P, N, C = map(int, input().split())

    if P == 0 and N == 0 and C == 0:
        break

    dados = ""

    for i in range(N):
        linha = input()

        for caractere in linha:
            if caractere == "0" or caractere == "1":
                dados += caractere

    resposta = 0

    for ponto in range(P):
        sequencia = 0

        for medicao in range(N):
            posicao = medicao * P + ponto

            if dados[posicao] == "1":
                sequencia += 1

                if sequencia == C:
                    resposta += 1

            else:
                sequencia = 0

    print(resposta)
