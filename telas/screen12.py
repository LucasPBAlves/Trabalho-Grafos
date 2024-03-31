from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState
from styles import DARK_THEME_STYLE

class Screen12(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Mostrar Matriz de Adjacência")
        self.setGeometry(100, 100, 800, 600)  # Ajustado para melhor visualização
        self.setStyleSheet(DARK_THEME_STYLE)  # Aplica o tema escuro global
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        instructionLabel = QLabel("Clique no botão abaixo para mostrar a Matriz de Adjacência do grafo.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        self.showMatrixButton = QPushButton("Mostrar Matriz de Adjacência", self)
        self.showMatrixButton.clicked.connect(self.showMatrix)
        layout.addWidget(self.showMatrixButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Tabela para exibir a matriz de adjacência
        self.matrixTable = QTableWidget(self)
        self.matrixTable.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)  # Desativa a edição

        # Atualiza a folha de estilo para o QTableWidget e QHeaderView para garantir visibilidade da grade branca
        self.matrixTable.setStyleSheet("""
            QHeaderView::section {
                background-color: transparent;  # Fundo transparente ou use #333333 para combinar com o tema
                color: white;  # Cor da fonte para combinar com o tema escuro
                border: 1px solid #ffffff;  # Define a borda dos cabeçalhos para branco
            }
            QTableWidget {
                gridline-color: #ffffff;  # Cor das linhas da grade branca para contraste
                color: white;  # Cor da fonte das células
                background-color: #333333;  # Cor de fundo das células
            }
            QTableWidget QTableCornerButton::section {
                background: #333333;  # Cor de fundo do canto superior esquerdo
            }
        """)

        layout.addWidget(self.matrixTable)

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)
    def showMatrix(self):
        arestas_str = SharedState.get_aresta()
        isDirected = SharedState.get_is_directed()

        if not arestas_str:
            print('Erro: Arestas não definidas')
            return

        arestas = arestas_str.split(';')
        vertices = set()

        for aresta in arestas:
            v1, v2 = aresta.split('-')
            vertices.add(v1)
            vertices.add(v2)

        vertices = sorted(list(vertices))
        num_vertices = len(vertices)
        self.matrixTable.setRowCount(num_vertices)
        self.matrixTable.setColumnCount(num_vertices)

        # Define cabeçalhos das linhas e colunas
        self.matrixTable.setHorizontalHeaderLabels(vertices)
        self.matrixTable.setVerticalHeaderLabels(vertices)

        # Ajusta o tamanho das células
        self.matrixTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.matrixTable.verticalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)

        vertex_to_index = {vertex: index for index, vertex in enumerate(vertices)}
        adjacencyMatrix = [[0] * num_vertices for _ in range(num_vertices)]

        for aresta in arestas:
            v1, v2 = aresta.split('-')
            idx1, idx2 = vertex_to_index[v1], vertex_to_index[v2]
            adjacencyMatrix[idx1][idx2] = 1
            if not isDirected:
                adjacencyMatrix[idx2][idx1] = 1

        # Preenche a tabela com a matriz
        for i, row in enumerate(adjacencyMatrix):
            for j, val in enumerate(row):
                self.matrixTable.setItem(i, j, QTableWidgetItem(str(val)))


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen12()
    screen.show()
    sys.exit(app.exec())