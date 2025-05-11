## Descrição do Projeto

Este projeto tem como objetivo resolver um labirinto bidimensional (2D) utilizando o algoritmo A\* (A-estrela), auxiliando um robô de resgate a encontrar o menor caminho entre dois pontos, evitando obstáculos e considerando o custo dos movimentos.

O robô começa no ponto **S** (start) e deve alcançar o ponto **E** (end), movendo-se apenas por células livres e em direções ortogonais (cima, baixo, esquerda, direita).

---

## Objetivos

- Implementar o algoritmo A\* com heurística de distância de Manhattan.
- Encontrar o menor caminho em uma matriz representando um labirinto.
- Exibir o caminho encontrado com coordenadas e visualmente dentro do labirinto.
- Validar a existência de **S** e **E** antes da execução.
- Retornar “Sem solução” caso não haja caminho possível.

---

## Entrada

A entrada é uma matriz 2D, com os seguintes valores:

- `S`: ponto inicial
- `E`: ponto final
- `0`: célula livre
- `1`: obstáculo

### Exemplo:

```
S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1
```

---

## Saída

Menor caminho (em coordenadas):

```
[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]
```

Labirinto com o caminho destacado:

```
S 0 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1

```

## Algoritmo A\*

O algoritmo A\* calcula o melhor caminho baseado na soma:

f(n) = g(n) + h(n)

Onde:

- `g(n)`: custo desde o ponto inicial até o ponto atual.
- `h(n)`: heurística (estimativa da distância até o fim) usando a distância de Manhattan:

h(n) = |x1 - x2| + |y1 - y2|

---

## Execução

### Requisitos

- Python 3 instalado

### Como executar

1. Clone este repositório
2. Execute o código:

```bash
python main.py
```

## Casos sem solução

Caso não exista caminho entre S e E, o programa exibirá:

```
Sem solução
```

## Integrantes do Grupo

- Daniel Estevam Pacheco de Souza

## Professor

- João Paulo Carneiro Aramuni
