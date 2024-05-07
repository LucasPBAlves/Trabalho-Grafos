from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QTableWidget, QTableWidgetItem, \
    QHeaderView, QSpacerItem, QSizePolicy, QMessageBox

from shared_state import SharedState
from styles import DARK_THEME_STYLE


class Screen13(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Representação de grafos utilizando Lista de Adjacência")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(DARK_THEME_STYLE)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        instructionLabel = QLabel("Clique no botão abaixo para gerar a Lista de Adjacência do grafo.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        buttonContainer = QHBoxLayout()
        buttonContainer.addItem(
            QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        testButton = QPushButton("Gerar Lista de Adjacência", self)
        testButton.clicked.connect(self.generateAdjacencyList)
        testButton.setFixedSize(400, 40)
        buttonContainer.addWidget(testButton)

        buttonContainer.addItem(
            QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonContainer)

        self.adjacencyListTable = QTableWidget(self)
        self.adjacencyListTable.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        layout.addWidget(self.adjacencyListTable)

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    def generateAdjacencyList(self):
        arestas_str = SharedState.get_aresta()
        if not arestas_str:
            QMessageBox.warning(self, "Aviso", "Não há arestas definidas no grafo.")
            self.adjacencyListTable.setRowCount(0)
            self.adjacencyListTable.setColumnCount(0)
            return

        isDirected = SharedState.get_is_directed()
        arestas = arestas_str.split(";")
        vertices = {}

        for aresta in arestas:
            try:
                v1, v2, weight = aresta.split('-')
                vertices.setdefault(v1, []).append(f"{v2} ({weight})")
                if not isDirected:
                    vertices.setdefault(v2, []).append(f"{v1} ({weight})")
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{aresta}' não está no formato correto.")

        self.adjacencyListTable.setRowCount(len(vertices))
        self.adjacencyListTable.setColumnCount(2)
        self.adjacencyListTable.setHorizontalHeaderLabels(["Vértice", "Lista de Adjacência"])

        for i, (vertex, adj_list) in enumerate(vertices.items()):
            self.adjacencyListTable.setItem(i, 0, QTableWidgetItem(vertex))
            self.adjacencyListTable.setItem(i, 1, QTableWidgetItem(", ".join(adj_list)))


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen13()
    screen.show()
    sys.exit(app.exec())
