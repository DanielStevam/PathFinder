import heapq

def heuristica(a, b):
    # Distância de Manhattan
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def encontrar_ponto(matriz, simbolo):
    for i, linha in enumerate(matriz):
        for j, valor in enumerate(linha):
            if valor == simbolo:
                return (i, j)
    return None

def a_estrela(matriz):
    inicio = encontrar_ponto(matriz, 'S')
    fim = encontrar_ponto(matriz, 'E')
    
    if not inicio or not fim:
        return "Erro: pontos S ou E não encontrados"

    aberta = []
    heapq.heappush(aberta, (0 + heuristica(inicio, fim), 0, inicio, [inicio]))
    visitados = set()

    while aberta:
        f, g, atual, caminho = heapq.heappop(aberta)
        if atual in visitados:
            continue
        visitados.add(atual)

        if atual == fim:
            return caminho

        vizinhos = [(0,1), (1,0), (0,-1), (-1,0)]  # direita, baixo, esquerda, cima

        for dx, dy in vizinhos:
            x, y = atual[0] + dx, atual[1] + dy
            if 0 <= x < len(matriz) and 0 <= y < len(matriz[0]):
                if matriz[x][y] != '1':
                    novo = (x, y)
                    if novo not in visitados:
                        heapq.heappush(aberta, (g + 1 + heuristica(novo, fim), g + 1, novo, caminho + [novo]))

    return "Sem solução"

def imprimir_labirinto(matriz, caminho):
    matriz_copia = [linha.copy() for linha in matriz]
    for x, y in caminho[1:-1]:
        matriz_copia[x][y] = '*'
    for linha in matriz_copia:
        print(' '.join(linha))

if __name__ == "__main__":
    labirinto = [
        ['S', '0', '1', '0', '0'],
        ['0', '0', '1', '0', '1'],
        ['1', '0', '1', '0', '0'],
        ['1', '0', '0', 'E', '1']
    ]
    caminho = a_estrela(labirinto)
    if isinstance(caminho, str):
        print(caminho)
    else:
        print("Menor caminho encontrado:")
        print(caminho)
        imprimir_labirinto(labirinto, caminho)
