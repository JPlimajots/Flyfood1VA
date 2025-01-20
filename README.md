# Projeto Fly Food - Otimização de Rotas

Este projeto foi desenvolvido como parte da primeira avaliação da disciplina **Projeto Interdisciplinar para Sistemas de Informação 2**. O objetivo principal é resolver um problema de otimização de rotas utilizando o método de força bruta. O programa lê uma matriz que representa os pontos de entrega de um drone, calcula todas as rotas possíveis entre os pontos e retorna o caminho mais eficiente, acompanhado de um gráfico ilustrativo.

## Funcionalidades

- Leitura de matrizes contendo a posição do ponto de partida e dos pontos de entrega.
- Cálculo de todas as permutações possíveis dos pontos de entrega.
- Determinação da rota com a menor distância total utilizando a distância de táxi (ou Manhattan).
- Geração de um gráfico representando a rota ótima encontrada.

## Pré-requisitos

Antes de executar o programa, certifique-se de que as seguintes bibliotecas estão instaladas em seu ambiente Python:

- `matplotlib`

Para instalar a biblioteca necessária, execute o seguinte comando no terminal:

```bash
pip install matplotlib
```

## Estrutura do Projeto

O projeto está organizado da seguinte forma:

```
.
├── matrizes/          # Diretório contendo os arquivos de matrizes
├── Fly_food_FB.py     # Código principal do programa
└── README.md          # Arquivo de documentação
```

## Como Executar o Programa

1. Coloque os arquivos de matriz no diretório `matrizes/`. Cada arquivo deve conter:
   - A primeira linha com o número de linhas e colunas da matriz.
   - A matriz propriamente dita, onde:
     - `R` representa o ponto de partida.
     - Letras diferentes de `R` representam os pontos de entrega.
     - `0` indica espaços vazios.

2. Execute o programa com o seguinte comando no terminal:

```bash
python Fly_food_FB.py
```

3. Siga as instruções para selecionar o arquivo de matriz desejado.

4. Após a execução, o programa exibirá:
   - O melhor caminho encontrado.
   - A distância total percorrida.
   - O tempo de execução.
   - Um gráfico ilustrando o trajeto.

## Exemplo de Arquivo de Matriz

Exemplo de arquivo `exemplo.txt` dentro do diretório `matrizes/`:

```
5 5
R 0 0 A 0
0 0 0 0 0
0 B 0 0 0
0 0 0 0 0
0 0 C 0 0
```

Neste exemplo:
- `R` é o ponto de partida.
- `A`, `B` e `C` são os pontos de entrega.
- O programa determinará a melhor rota para passar por todos os pontos e retornar ao ponto de partida.

## Contribuidores

- André Barbosa
- João Pedro de Lima
- Márcia Alves de Assis Lima
- Wilka Vitória Granjeiro do Nascimento

## Licença

Este projeto foi desenvolvido para fins acadêmicos e é de uso exclusivo para aprendizado na disciplina "Projeto Interdisciplinar para Sistemas de Informação 2".
