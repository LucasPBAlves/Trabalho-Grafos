class GrafoListaAdjacencia:
    def __init__(self, num_vertices, direcionado=True):
        self.num_vertices = num_vertices
        self.direcionado = direcionado
        self.lista_adjacencia = {i: [] for i in range(num_vertices)}

    def adicionar_aresta(self, origem, destino):
        self.lista_adjacencia[origem].append(destino)
        if not self.direcionado:
            self.lista_adjacencia[destino].append(origem)

    def remover_aresta(self, origem, destino):
        self.lista_adjacencia[origem].remove(destino)
        if not self.direcionado:
            self.lista_adjacencia[destino].remove(origem)

    def imprimir_lista(self):
        for vertice, vizinhos in self.lista_adjacencia.items():
            print(f"{vertice}: {vizinhos}")

    def vizinhanca_vertice(self, vertice):
        return self.lista_adjacencia[vertice]

    def grau_vertice(self, vertice):
        grau = len(self.lista_adjacencia[vertice])
        if not self.direcionado:
            for vizinho in self.lista_adjacencia[vertice]:
                if vizinho == vertice:
                    grau += 1
        return grau

    def is_simple(self):
        for vertice, vizinhos in self.lista_adjacencia.items():
            if vertice in vizinhos:
                return False
            for vizinho in vizinhos:
                if vizinho == vertice or self.lista_adjacencia[vizinho].count(vertice) > 1:
                    return False
        return True

    def is_regular(self):
        grau_base = self.grau_vertice(0)
        for i in range(1, self.num_vertices):
            if self.grau_vertice(i) != grau_base:
                return False
        return True

    def is_completo(self):
        for vertice, vizinhos in self.lista_adjacencia.items():
            if len(vizinhos) != self.num_vertices - 1:
                return False
        return True

    def is_bipartido(self):
        # Implementação do teste de bipartição não é trivial utilizando lista de adjacência
        return False
