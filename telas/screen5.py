from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QMessageBox)
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState

class Screen5(QDialog):
    backSignal = pyqtSignal()
    nextSignal = pyqtSignal()  # Se necessário, para navegação adicional

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Identificação da Vizinhança de um Vértice")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Identificação da Vizinhança de um Vértice", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Campo de entrada para o vértice de interesse
        self.vertexInput = QLineEdit(self)
        self.vertexInput.setPlaceholderText("Insira o vértice")
        layout.addWidget(self.vertexInput)

        # Botão para identificar vizinhança
        identifyButton = QPushButton("Identificar Vizinhança", self)
        identifyButton.clicked.connect(self.identifyNeighborhood)
        layout.addWidget(identifyButton)

        # Área para exibir a vizinhança
        self.neighborhoodLabel = QLabel("", self)
        self.neighborhoodLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.neighborhoodLabel)

        # Botão Voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton)

        self.setLayout(layout)

    def identifyNeighborhood(self):
        vertex = self.vertexInput.text().strip()
        if not vertex:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, insira o vértice.")
            return
        arestas = SharedState.get_aresta()
        neighborhood = set()
        for aresta in arestas.split(';'):
            v1, v2 = aresta.split('-')
            if v1 == vertex:
                neighborhood.add(v2)
            elif v2 == vertex:
                neighborhood.add(v1)
        self.neighborhoodLabel.setText(f"Vizinhança de {vertex}: {', '.join(neighborhood)}")

