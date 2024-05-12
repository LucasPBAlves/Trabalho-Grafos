# Trabalho de Grafos

***Trabalho de Vizualização de Grafos para a matéria de Grafos, 5° período de Engenharia da Computação da PUC Minas***

# Implementação de Grafos com PyQt6

Este repositório contém o código-fonte de uma aplicação de manipulação de grafos, desenvolvida em Python e utilizando a
biblioteca gráfica PyQt6. A aplicação oferece funcionalidades como a criação e visualização de grafos, adição e remoção
de arestas, análise de propriedades dos grafos, e representações em Matriz de Adjacência e Lista de Adjacência.

## Sobre o Projeto

O objetivo deste projeto é fornecer uma ferramenta interativa para a criação e análise de grafos, permitindo aos
usuários testar diferentes propriedades e representações de forma visual e intuitiva. O projeto foi desenvolvido como
parte de um trabalho acadêmico sobre estruturas de dados e teoria dos grafos.

## Autores

- **Lucas Pimenta Brito Alves**
- **Caio José da Silva**

## Funcionalidades

- Criação de um grafo com um número definido de vértices.
- Adição e remoção de arestas entre os vértices.
- Identificação e visualização da vizinhança de um vértice.
- Análise de sucessores e predecessores em grafos direcionados.
- Cálculo do grau dos vértices.
- Verificação se o grafo é simples, regular, completo, ou bipartido.
- Representação do grafo através de Matriz de Adjacência e Lista de Adjacência.

## Pré-requisitos

Para executar o projeto, você precisará ter instalado em seu sistema:

- Python 3.x
- PyQt6

Você pode instalar a PyQt6 usando o pip, o gerenciador de pacotes do Python:

```bash
pip install PyQt6
```

## Como Executar

Para rodar a aplicação, clone o repositório para sua máquina local e execute o arquivo principal:

```bash
git clone https://github.com/LucasPBAlves/Trabalho-Grafos
cd Trabalho-Grafos
python main.py
```

## Navegação das Telas e Funcionalidades

### Tela Inicial

- **Criação de um grafo com X vértices**: Permite ao usuário iniciar a criação de um novo grafo, especificando o número
  de vértices.
- **Usar grafos já plotados**: Função ainda não implementada.

### Tela 1: Criação de um grafo com X vértices

Permite ao usuário especificar o número de vértices do grafo a ser criado. Após definir o número de vértices, o usuário
avança para decidir se o grafo será direcionado ou não.

### Tela 2: Definição do Tipo de Grafo

Nesta tela, o usuário decide se o grafo a ser criado será direcionado ou não direcionado. Essa escolha influenciará as
opções disponíveis nas etapas seguintes, especialmente na análise de propriedades específicas do grafo.

### Tela 3: Adição e Remoção de Arestas

Após definir o tipo do grafo, o usuário pode adicionar ou remover arestas entre os vértices especificados. Essa tela
fornece flexibilidade para modelar o grafo conforme necessário, permitindo ajustes na estrutura de arestas.

### Tela 4: Menu de Operações

A partir daqui, o usuário é apresentado a um menu com diversas operações e análises que podem ser realizadas sobre o
grafo criado, incluindo:

- **Identificação da vizinhança de um vértice** (para grafos não direcionados).
- **Identificação dos sucessores e predecessores de um vértice** (para grafos direcionados).
- **Identificação do grau de um determinado vértice**, **testes de propriedades do grafo** (simples, regular, completo,
  bipartido), e **representações do grafo** (usando matriz de adjacência ou lista de adjacência).

### Telas de Análise e Representação

Cada opção de análise ou representação selecionada no menu de operações leva a uma tela específica onde o usuário pode
fornecer dados adicionais necessários (como o vértice de interesse) e visualizar os resultados ou representações
gerados.

Aqui está o README atualizado com a inclusão das novas telas e funcionalidades implementadas:
Trabalho de Grafos

Trabalho de Vizualização de Grafos para a matéria de Grafos, 5° período de Engenharia da Computação da PUC Minas
Implementação de Grafos com PyQt6

Este repositório contém o código-fonte de uma aplicação de manipulação de grafos, desenvolvida em Python e utilizando a biblioteca gráfica PyQt6. A aplicação oferece funcionalidades como a criação e visualização de grafos, adição e remoção de arestas, análise de propriedades dos grafos, e representações em Matriz de Adjacência e Lista de Adjacência.
Sobre o Projeto

O objetivo deste projeto é fornecer uma ferramenta interativa para a criação e análise de grafos, permitindo aos usuários testar diferentes propriedades e representações de forma visual e intuitiva. O projeto foi desenvolvido como parte de um trabalho acadêmico sobre estruturas de dados e teoria dos grafos.
Autores

    Lucas Pimenta Brito Alves
    Caio José da Silva

Funcionalidades

    Criação de um grafo com um número definido de vértices.
    Adição e remoção de arestas entre os vértices.
    Identificação e visualização da vizinhança de um vértice.
    Análise de sucessores e predecessores em grafos direcionados.
    Cálculo do grau dos vértices.
    Verificação se o grafo é simples, regular, completo, ou bipartido.
    Representação do grafo através de Matriz de Adjacência e Lista de Adjacência.
    Busca em largura (BFS).
    Busca em profundidade (DFS).
    Ordenação Topológica.
    Árvore Geradora Mínima (AGM) usando Prim ou Kruskal.
    Teste de conectividade do grafo.
    Identificação do caminho mínimo entre dois vértices (Dijkstra).

Pré-requisitos

Para executar o projeto, você precisará ter instalado em seu sistema:

    Python 3.x
    PyQt6

Você pode instalar a PyQt6 usando o pip, o gerenciador de pacotes do Python:

bash

pip install PyQt6

Como Executar

Para rodar a aplicação, clone o repositório para sua máquina local e execute o arquivo principal:

bash

git clone https://github.com/LucasPBAlves/Trabalho-Grafos
cd Trabalho-Grafos
python main.py

Navegação das Telas e Funcionalidades
Tela Inicial

    Criação de um grafo com X vértices: Permite ao usuário iniciar a criação de um novo grafo, especificando o número de vértices.
    Usar grafos já plotados: Função ainda não implementada.

Tela 1: Criação de um grafo com X vértices

Permite ao usuário especificar o número de vértices do grafo a ser criado. Após definir o número de vértices, o usuário avança para decidir se o grafo será direcionado ou não.
Tela 2: Definição do Tipo de Grafo

Nesta tela, o usuário decide se o grafo a ser criado será direcionado ou não direcionado. Essa escolha influenciará as opções disponíveis nas etapas seguintes, especialmente na análise de propriedades específicas do grafo.
Tela 3: Adição e Remoção de Arestas

Após definir o tipo do grafo, o usuário pode adicionar ou remover arestas entre os vértices especificados. Essa tela fornece flexibilidade para modelar o grafo conforme necessário, permitindo ajustes na estrutura de arestas.
Tela 4: Menu de Operações

A partir daqui, o usuário é apresentado a um menu com diversas operações e análises que podem ser realizadas sobre o grafo criado, incluindo:

    Identificação da vizinhança de um vértice (para grafos não direcionados).
    Identificação dos sucessores e predecessores de um vértice (para grafos direcionados).
    Identificação do grau de um determinado vértice, testes de propriedades do grafo (simples, regular, completo, bipartido), e representações do grafo (usando matriz de adjacência ou lista de adjacência).

### Telas de Análise e Representação

Cada opção de análise ou representação selecionada no menu de operações leva a uma tela específica onde o usuário pode fornecer dados adicionais necessários (como o vértice de interesse) e visualizar os resultados ou representações gerados.

### Novas Telas e Funcionalidades

    Tela 14: Busca em Largura (BFS): Permite realizar uma busca em largura a partir de um vértice especificado.
    Tela 15: Busca em Profundidade (DFS): Permite realizar uma busca em profundidade a partir de um vértice especificado.
    Tela 16: Ordenação Topológica: Permite realizar a ordenação topológica dos vértices de um grafo direcionado acíclico (DAG).
    Tela 17: Árvore Geradora Mínima (AGM): Permite calcular a árvore geradora mínima utilizando o algoritmo de Kruskal.
    Tela 18: Teste de Conectividade: Permite verificar se o grafo é conexo.
    Tela 19: Caminho Mínimo (Dijkstra): Permite encontrar o caminho mínimo entre dois vértices utilizando o algoritmo de Dijkstra.