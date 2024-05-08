from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox
from collections import defaultdict

from shared_state import SharedState
from fila import Fila

class Screen14(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Busca em Largura (BFS)")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Espaçadores para centralizar na vertical
        layout.addItem(QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Centralizando o instructionLabel
        instructionLabel = QLabel("Insira o vértice inicial para a Busca em Largura:", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Layout horizontal para manter caixa de texto e botão no centro
        inputLayout = QVBoxLayout()
        inputLayout.addWidget(instructionLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        # Caixa de texto centralizada e ajustada
        self.vertexInput = QLineEdit(self)
        self.vertexInput.setPlaceholderText("Vértice inicial")
        self.vertexInput.setFixedSize(200, 40)
        inputLayout.addWidget(self.vertexInput, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botão de testar BFS
        testButton = QPushButton("Testar BFS", self)
        testButton.setFixedSize(200, 40)
        testButton.clicked.connect(self.performBFS)
        inputLayout.addWidget(testButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Resultado da busca em largura
        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        inputLayout.addWidget(self.resultLabel, alignment=Qt.AlignmentFlag.AlignCenter)

        # Adicionar layout com os widgets ao layout principal
        layout.addLayout(inputLayout)

        # Espaçador inferior para centralizar verticalmente
        layout.addItem(QSpacerItem(20, 80, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Botão Voltar
        backButtonLayout = QHBoxLayout()
        backButtonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        backButton = QPushButton("Voltar", self)
        backButton.setFixedSize(100, 40)
        backButton.clicked.connect(self.backSignal.emit)
        backButtonLayout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(backButtonLayout)

        self.setLayout(layout)

    def performBFS(self):
        start_vertex = self.vertexInput.text().strip()
        if not start_vertex:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, insira um vértice inicial para a busca.")
            return

        edges_str = SharedState.get_aresta()
        if not edges_str:
            QMessageBox.warning(self, "Erro", "Não há arestas definidas no grafo.")
            return

        graph = defaultdict(list)
        vertices = set()

        for edge in edges_str.split(';'):
            v1, v2, _ = edge.split('-')
            graph[v1].append(v2)
            if not SharedState.get_is_directed():
                graph[v2].append(v1)
            vertices.update([v1, v2])

        if start_vertex not in vertices:
            QMessageBox.warning(self, "Erro", "O vértice inicial não existe no grafo.")
            return

        fila = Fila(len(vertices))  # Usando a classe Fila implementada
        visited = set()
        order = []

        fila.inserir(start_vertex)

        while not fila.is_vazia():
            vertex = fila.remover()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        fila.inserir(neighbor)

        self.resultLabel.setText("Ordem de visita: " + " -> ".join(order))

if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen14()
    screen.show()
    sys.exit(app.exec())
