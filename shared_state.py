class SharedState:
    _instance = None
    vertices_count = 0
    is_directed = False  # Adicionado novo atributo

    @staticmethod
    def getInstance():
        if SharedState._instance is not None:
            SharedState._instance = SharedState()
        return SharedState._instance

    @classmethod
    def setVerticesCount(cls, count):
        cls.vertices_count = count
        print("cls set V", cls.vertices_count)

    @classmethod
    def getVerticesCount(cls):
        print("cls Get V", cls.vertices_count)
        return cls.vertices_count


    @classmethod
    def setIsDirected(cls, directed):
        cls.is_directed = directed
        print("cls set D",cls.is_directed)

    @classmethod
    def getIsDirected(cls):
        print("cls Get D", cls.is_directed)
        return cls.is_directed
