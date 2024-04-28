class Fila:
    def __init__(self, tamanho=6):
        self.array = [0] * (tamanho + 1)
        self.primeiro = 0  # Remove do índice "primeiro".
        self.ultimo = 0  # Insere no índice "ultimo".

    def inserir(self, x):
        # Validar inserção
        if (self.ultimo + 1) % len(self.array) == self.primeiro:
            raise Exception("Erro ao inserir!")

        self.array[self.ultimo] = x
        self.ultimo = (self.ultimo + 1) % len(self.array)

    def remover(self):
        # Validar remoção
        if self.primeiro == self.ultimo:
            raise Exception("Erro ao remover!")

        resp = self.array[self.primeiro]
        self.primeiro = (self.primeiro + 1) % len(self.array)
        return resp

    def mostrar(self):
        print("[", end=" ")

        i = self.primeiro
        while i != self.ultimo:
            print(self.array[i], end=" ")
            i = (i + 1) % len(self.array)

        print("]")

    def mostrar_rec(self):
        print("[", end=" ")
        self.mostrar_rec_aux(self.primeiro)
        print("]")

    def mostrar_rec_aux(self, i):
        if i != self.ultimo:
            print(self.array[i], end=" ")
            self.mostrar_rec_aux((i + 1) % len(self.array))

    def is_vazia(self):
        return self.primeiro == self.ultimo
