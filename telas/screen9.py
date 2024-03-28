from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal
from collections import defaultdict
from shared_state import SharedState

class Screen9(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o Grafo é Regular")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Clique para testar se o grafo é regular:", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        testButton = QPushButton("Testar Regularidade", self)
        testButton.clicked.connect(self.testRegularity)
        layout.addWidget(testButton)

        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    def testRegularity(self):
        arestas = SharedState.get_aresta().split(';')
        grau_vertices = defaultdict(int)

        for aresta in arestas:
            v1, v2 = aresta.split('-')
            grau_vertices[v1] += 1
            grau_vertices[v2] += 1

        graus = set(grau_vertices.values())

        if len(graus) == 1:
            self.resultLabel.setText(f"O grafo é regular com grau {graus.pop()}.")
        else:
            self.resultLabel.setText("O grafo não é regular.")

