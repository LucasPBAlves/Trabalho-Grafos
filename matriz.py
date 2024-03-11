class GrafoMatrizAdjacencia:
    def __init__(self, num_vertices, direcionado=True):
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.matriz_adjacencia = [[0] * num_vertices for _ in range(num_vertices)]

    def adicionar_aresta(self, origem, destino):
        self.matriz_adjacencia[origem][destino] = 1
        if not self.direcionado:
            self.matriz_adjacencia[destino][origem] = 1

    def remover_aresta(self, origem, destino):
        self.matriz_adjacencia[origem][destino] = 0
        if not self.direcionado:
            self.matriz_adjacencia[destino][origem] = 0

    def imprimir_matriz(self):
        for linha in self.matriz_adjacencia:
            print(linha)

    def vizinhanca_vertice(self, vertice):
        vizinhanca = []
        for i in range(self.num_vertices):
            if self.matriz_adjacencia[vertice][i] == 1:
                vizinhanca.append(i)
        return vizinhanca

    def grau_vertice(self, vertice):
        grau = sum(self.matriz_adjacencia[vertice])
        if not self.direcionado:
            grau += self.matriz_adjacencia[vertice][vertice]
        return grau

    def is_simple(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if i == j and self.matriz_adjacencia[i][j] != 0:
                    return False
                if self.matriz_adjacencia[i][j] > 1:
                    return False
        return True

    def is_regular(self):
        grau_base = self.grau_vertice(0)
        for i in range(1, self.num_vertices):
            if self.grau_vertice(i) != grau_base:
                return False
        return True

    def is_completo(self):
        for i in range(self.num_vertices):
            for j in range(self.num_vertices):
                if i != j and self.matriz_adjacencia[i][j] != 1:
                    return False
        return True

    def is_bipartido(self):
        # Implementação do teste de bipartição não é trivial utilizando matriz de adjacência
        return False