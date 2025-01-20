'''Projeto Fly food - Forca Bruta - Equipe: Andre, Breno, Joao Pedro, Marcia e Wilka'''


def matrizes(dir_mat):
    import os
    dic_matrizes = {str(i + 1): arquivo for i,
                    arquivo in enumerate(sorted(os.listdir(dir_mat)))}
    return dic_matrizes


def sel_arq_matriz(dir_mat):
    dic_matrizes = matrizes(dir_mat)
    print('Matrizes localizadas: \n')
    for numero, arquivo in dic_matrizes.items():
        print(f'{numero} - {arquivo}')
    print()
    num_matriz = 0
    while num_matriz not in dic_matrizes:  # Escolha da matriz que sera testada
        num_matriz = input('Informe o número da matriz que deseja analisar: ')
    return dic_matrizes[num_matriz]

# Calculo da geometria do taxi


def geo_taxi(x1, y1, x2, y2):
    # Distancia horizontal + distancia vertical
    d = abs((x2-x1)) + abs((y2-y1))
    return d

# Calculo das permutacoes recursivamente


def permutacoes(lista):
    if len(lista) == 0:     # Caso base (lista vazia)
        return [[]]
    calc_permut = []
    for i in range(len(lista)):
        # Para cada elemento da lista, gera permutacoes dos elementos restantes
        # Remove o elemento atual
        restante = lista[:i] + lista[i+1:]
        # Chama a funcao recursivamente
        for permutacao in permutacoes(restante):
            # Adiciona o elemento atual a permutacao
            calc_permut.append([lista[i]] + permutacao)
    return calc_permut


def rota(pt_a, pt_b, visitados):
    coordenadas = []                        # Coordenadas do caminho
    # Obtém as coordenadas x e y do ponto A
    pt_a_x, pt_a_y = pt_a[0], pt_a[1]

    # Obtém as coordenadas x e y do ponto B
    pt_b_x, pt_b_y = pt_b[0], pt_b[1]

    x = pt_a_x      # Define a coordenada x inicial
    y = pt_a_y      # Define a coordenada y inicial
    p = pt_a        # Ponto atual começa em pt_a

    # Define a direção do movimento vertical (para cima ou para baixo)
    step = 1 if pt_a_y <= pt_b_y else -1
    # Move verticalmente de pt_a para pt_b
    for i in range(pt_a_y + step, pt_b_y + step, step):
        # Atualiza o ponto atual para a nova posição
        p = (x, i)
        if not p in visitados:                          # Verifica se o ponto já foi visitado
            # Adiciona o ponto à lista de coordenadas
            coordenadas.append(p)
            # Marca o ponto como visitado
            visitados.append(p)
            if p == pt_b:                               # Se chegou ao ponto B, retorna as coordenadas
                return coordenadas
            y = i                                       # Atualiza y para a nova posição
        else:
            break                                       # Se o ponto foi visitado, sai do loop

    # Define a direção do movimento horizontal (para a esquerda ou para a direita)
    step = 1 if pt_a_x <= pt_b_x else -1
    # Move horizontalmente de pt_a para pt_b
    for i in range(pt_a_x + step, pt_b_x + step, step):
        # Atualiza o ponto atual para a nova posição
        p = (i, y)
        if not p in visitados:                          # Verifica se o ponto já foi visitado
            # Adiciona o ponto à lista de coordenadas
            coordenadas.append(p)
            # Marca o ponto como visitado
            visitados.append(p)
            if p == pt_b:                               # Se chegou ao ponto B, retorna as coordenadas
                return coordenadas
        else:
            break                                       # Se o ponto foi visitado, sai do loop

    # Chama recursivamente a função para continuar a rota a partir do ponto atual
    return coordenadas + rota(p, pt_b, visitados)


def rota_completa(caminho, coord_pts):
    visitados = []                                      # Pontos já visitados
    # Ponto de partida (origem)
    pt_r = (0, 0)
    # Inicia a lista de coordenadas com o ponto de partida
    coordenadas = [pt_r]

    # Obtém o primeiro ponto do caminho
    p0 = coord_pts[caminho[0]]
    # Move do ponto de partida ao primeiro ponto
    coordenadas += rota(pt_r, p0, visitados)

    for n in range(len(caminho) - 1):                   # Move entre os pontos do caminho
        pt_n = coord_pts[caminho[n]]                    # Ponto atual
        pt_n1 = coord_pts[caminho[n + 1]]               # Próximo ponto
        coordenadas += rota(pt_n, pt_n1, visitados)     # Move entre os pontos

    # Último ponto no caminho
    pt_ult = coord_pts[caminho[-1]]
    # Retorna ao ponto de partida
    coordenadas += rota(pt_ult, pt_r, visitados)

    # Lista completa de coordenadas
    return coordenadas


def plotar(caminho, coord_pts):
    # Obtém todas as coordenadas do caminho
    coordenadas = rota_completa(caminho, coord_pts)
    # Retornando ao ponto 'R'        # Adiciona o ponto de partida para fechar o caminho
    coordenadas.append((0, 0))
    x_coords, y_coords = [], []
    for ponto in coordenadas:
        x_coords.append(ponto[0])
        y_coords.append(ponto[1])

    # Criacao do grafico da rota
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    # Plota a rota com marcadores nos pontos
    plt.plot(x_coords, y_coords, marker='o', linestyle='-')
    plt.title('Rota do Drone')  # Titulo do grafico
    plt.xlabel('Coordenada X')  # Rotulo do eixo X
    plt.ylabel('Coordenada Y')  # Rotulo do eixo Y

    # Adiciona os pontos de entrega ao grafico
    for ponto, (x, y) in coord_pts.items():
        # Adiciona o texto com o nome do ponto
        plt.text(x, y, ponto, fontsize=12, ha='right')

    plt.grid()  # Adiciona uma grade ao grafico
    plt.show()  # Exibe o grafico


def main():
    dir_mat = 'matrizes'
    arq_matriz = sel_arq_matriz(dir_mat)

    # Lendo o arquivo da matriz
    with open(f'{dir_mat}/{arq_matriz}', 'r') as file:
        linhas = file.read().splitlines()

    # Definindo o número de linhas e colunas da matriz
    num_linhas_matriz, num_colunas_matriz = [int(x) for x in linhas[0].split()]
    # Lê a matriz a partir da segunda linha do arquivo
    matriz = [linha.split() for linha in linhas[1: num_linhas_matriz + 1]]

    # Início da execução do cálculo de caminhos
    import time
    start_time = time.time()

    # Busca na matriz e guarda as coordenadas dos pontos em um dici1onario
    # Armazena letras diferentes de '0' (pontos de entrega)
    pts_entrega = []
    coord_pts = {}        # Armazena coordenadas dos pontos

    # Itera sobre a matriz para encontrar os pontos de entrega e suas coordenadas
    for l in range(num_linhas_matriz):
        for c in range(num_colunas_matriz):
            # Obtem a letra na posicao (x, y)
            letra = matriz[l][c]
            if letra != '0':                    # Armazena a coordenada se for diferente de '0'
                x = c
                # O número da linha é o inverso da coordenada y
                y = (num_linhas_matriz - 1) - l
                # Armazena a coordenada em forma de tupla
                coord_pts[letra] = (x, y)
                if letra != 'R':                # Adiciona as letras diferentes de 'R' na lista
                    pts_entrega.append(letra)

    # Calculo das permutacoes dos elementos de entrega
    perm_pts = permutacoes(pts_entrega)  # Gera todas as permutacoes das letras

    # Busca pelo melhor caminho
    # Inicia com infinito para garantir que qualquer distancia encontrada seja a menor
    dist_menor_caminho = float('inf')
    menor_caminho = []

    # Coordenadas do ponto de partida R
    pt_r_x, pt_r_y = 0, 0

    # Calculo das distancias e busca do melhor caminho
    for caminho in perm_pts:
        soma_dist = 0       # Soma das distancias para o caminho atual

        # Coordenadas do primeiro ponto do caminho
        pt_0 = caminho[0]
        pt_0_x, pt_0_y = coord_pts[pt_0][0], coord_pts[pt_0][1]

        # Distancia do ponto 'R' ao primeiro ponto do camjnho
        soma_dist += geo_taxi(pt_r_x, pt_r_y, pt_0_x, pt_0_y)

        # Distancias entre os pontos na permutacao
        for x in range(len(caminho) - 1):
            pt_a = caminho[x]       # Ponto atual
            pt_a_x, pt_a_y = coord_pts[pt_a][0], coord_pts[pt_a][1]

            pt_b = caminho[x + 1]   # Proximo ponto
            pt_b_x, pt_b_y = coord_pts[pt_b][0], coord_pts[pt_b][1]

            soma_dist += geo_taxi(pt_a_x, pt_a_y, pt_b_x, pt_b_y)

        # Distancia do ultimo ponto de volta ao ponto 'R'
        pt_ult = caminho[-1]
        pt_ult_x, pt_ult_y = coord_pts[pt_ult][0], coord_pts[pt_ult][1]
        soma_dist += geo_taxi(pt_ult_x, pt_ult_y, pt_r_x, pt_r_y)

        # Atualiza o melhor caminho se a soma das distancias for menor
        if soma_dist < dist_menor_caminho:
            dist_menor_caminho = soma_dist    # Atualiza a menor distancia encontrada
            menor_caminho = caminho           # Atualiza o melhor caminho

    # Fim da execução do cálculo de rota
    end_time = time.time()
    tempo_execucao = end_time - start_time

    # Exibe o melhor caminho e a distancia total
    print(" ".join(menor_caminho), dist_menor_caminho)
    print("Tempo de execucao:", tempo_execucao, "segundos")

    # Plotagem da rota do caminho
    plotar(menor_caminho, coord_pts)


if __name__ == '__main__':
    main()
