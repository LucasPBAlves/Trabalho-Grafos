class SharedState:
    _instance = None
    vertices_count = 0
    is_directed = False  # Adicionado novo atributo
    arestas = []

    @staticmethod
    def get_instance():
        if SharedState._instance is not None:
            SharedState._instance = SharedState()
        return SharedState._instance

    @classmethod
    def set_vertices_count(cls, count):
        cls.vertices_count = count
        print("cls set V", cls.vertices_count)

    @classmethod
    def get_vertices_count(cls):
        print("cls Get V", cls.vertices_count)
        return cls.vertices_count

    @classmethod
    def set_is_directed(cls, directed):
        cls.is_directed = directed
        print("cls set D", cls.is_directed)

    @classmethod
    def get_is_directed(cls):
        print("cls Get D", cls.is_directed)
        return cls.is_directed

    @classmethod
    def set_aresta(cls, aresta):
        cls.arestas = aresta
        print("Set Aresta", cls.arestas)

    @classmethod
    def get_aresta(cls):
        print("Get Aresta", cls.arestas)
        return cls.arestas
