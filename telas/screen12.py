from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QGridLayout
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState

class Screen12(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Representação de Grafos utilizando Matriz de Adjacência")
        self.setGeometry(100, 100, 600, 400)
        self.matrixLabel = QLabel("", self)  # Label para mostrar a matriz
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        titleLabel = QLabel("Matriz de Adjacência do Grafo", self)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(titleLabel)

        generateMatrixButton = QPushButton("Gerar Matriz de Adjacência", self)
        generateMatrixButton.clicked.connect(self.generateAdjacencyMatrix)
        layout.addWidget(generateMatrixButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Configurações do label de matriz
        self.matrixLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.matrixLabel)

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def generateAdjacencyMatrix(self):
        # Obtém as arestas do SharedState
        edges = SharedState.get_aresta()
        # Constrói a matriz de adjacência
        matrix = self.buildAdjacencyMatrix(edges)
        # Converte a matriz para uma string formatada para exibição
        matrixStr = self.matrixToString(matrix)
        self.matrixLabel.setText(matrixStr)

    def buildAdjacencyMatrix(self, edges):
        vertices = set()
        for edge in edges:
            v1, v2 = edge.split('->')
            vertices.add(v1)
            vertices.add(v2)
        vertices = sorted(list(vertices))
        size = len(vertices)
        matrix = [[0] * size for _ in range(size)]
        vertexIndex = {v: i for i, v in enumerate(vertices)}
        for edge in edges:
            v1, v2 = edge.split('->')
            matrix[vertexIndex[v1]][vertexIndex[v2]] = 1
            # Para grafos não direcionados, marque também a aresta inversa
            if not SharedState.get_is_directed():
                matrix[vertexIndex[v2]][vertexIndex[v1]] = 1
        return matrix

    def matrixToString(self, matrix):
        matrixStr = '\n'.join([' '.join(map(str, row)) for row in matrix])
        return matrixStr

if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen12()
    screen.show()
    sys.exit(app.exec())
