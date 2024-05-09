def ler_matriz():
    linhas = int(input())
    colunas = int(input())
    matriz = []
    for _ in range(linhas):
        linha = list(map(int, input().split()))
        matriz.append(linha)
    return matriz
def contar_bombas_vizinhanca(matriz, linha, coluna):
    linhas = len(matriz)
    colunas = len(matriz[0])
    count = 0
    for i in range(max(0, linha - 1), min(linhas, linha + 2)):
        for j in range(max(0, coluna - 1), min(colunas, coluna + 2)):
            if (i, j) != (linha, coluna) and matriz[i][j] == 1:
                count += 1
    return count
matriz = ler_matriz()
linha = int(input("Digite a linha da célula: "))
coluna = int(input("Digite a coluna da célula: "))
vizinhanca = contar_bombas_vizinhanca(matriz, linha, coluna)
print(vizinhanca)