from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QMessageBox
from collections import defaultdict

from shared_state import SharedState
from pilha import Pilha

class Screen15(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Busca em Profundidade (DFS)")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Espaço expansível superior
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Instrução e caixa de texto para o vértice inicial
        instructionLabel = QLabel("Insira o vértice inicial para a Busca em Profundidade:", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        self.vertexInput = QLineEdit(self)
        self.vertexInput.setPlaceholderText("Vértice inicial")
        self.vertexInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.vertexInput.setMaximumWidth(200)
        layout.addWidget(self.vertexInput, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botão para testar a busca
        testButton = QPushButton("Testar DFS", self)
        testButton.clicked.connect(self.performDFS)
        layout.addWidget(testButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Etiqueta para mostrar resultados
        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        # Espaço expansível inferior
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Botão para voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def performDFS(self):
        start_vertex = self.vertexInput.text().strip()
        if not start_vertex:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, insira um vértice inicial para a busca.")
            return

        edges_str = SharedState.get_aresta()
        is_directed = SharedState.get_is_directed()
        if not edges_str:
            QMessageBox.warning(self, "Erro", "Não há arestas definidas no grafo.")
            return

        graph = defaultdict(list)
        vertices = set()

        for edge in edges_str.split(';'):
            v1, v2, _ = edge.split('-')
            graph[v1].append(v2)
            if not is_directed:
                graph[v2].append(v1)
            vertices.update([v1, v2])

        if start_vertex not in vertices:
            QMessageBox.warning(self, "Erro", "O vértice inicial não existe no grafo.")
            return

        visited = set()
        stack = Pilha()
        stack.push(start_vertex)
        order = []

        while not stack.isVazia():
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                order.append(vertex)
                for neighbor in reversed(graph[vertex]):
                    if neighbor not in visited:
                        stack.push(neighbor)

        self.resultLabel.setText("Ordem de visita: " + " -> ".join(order))

if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen15()
    screen.show()
    sys.exit(app.exec())
