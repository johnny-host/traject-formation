n = int(input())
secoes = list(map(int, input().split()))
meta = sum(secoes) / 2
soma_atual = 0

for i in range(n):
    soma_atual += secoes[i]
    if soma_atual == meta:
        print(i + 1)
        break
