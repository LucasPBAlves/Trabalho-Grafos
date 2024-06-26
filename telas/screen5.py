from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QMessageBox,
                             QSpacerItem, QSizePolicy)

from shared_state import SharedState


class Screen5(QDialog):
    backSignal = pyqtSignal()

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

        inputLayout = QHBoxLayout()
        inputLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        self.vertexInput = QLineEdit(self)
        self.vertexInput.setPlaceholderText("Insira o vértice")
        self.vertexInput.setFixedSize(200, 40)
        inputLayout.addWidget(self.vertexInput)

        inputLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(inputLayout)

        buttonLayout = QHBoxLayout()
        buttonLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        identifyButton = QPushButton("Identificar Vizinhança", self)
        identifyButton.setFixedSize(200, 40)
        identifyButton.clicked.connect(self.identifyNeighborhood)
        buttonLayout.addWidget(identifyButton)

        buttonLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

        self.neighborhoodLabel = QLabel("", self)
        self.neighborhoodLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.neighborhoodLabel)

        backButton = QPushButton("Voltar", self)
        backButton.setFixedSize(200, 40)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)
        backButton.clicked.connect(self.backSignal.emit)

        self.setLayout(layout)

    def identifyNeighborhood(self):
        vertex = self.vertexInput.text().strip()
        if not vertex:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, insira o vértice.")
            return

        arestas = SharedState.get_aresta()
        neighborhood = set()

        for aresta in arestas.split(';'):
            try:
                v1, v2, _ = aresta.split('-')
                if v1 == vertex or v2 == vertex:
                    neighborhood.add(v1 if v1 != vertex else v2)
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{aresta}' não está no formato correto.")

        if neighborhood:
            self.neighborhoodLabel.setText(f"Vizinhança de {vertex}: {', '.join(sorted(neighborhood))}")
        else:
            self.neighborhoodLabel.setText(f"Vértice {vertex} não encontrado.")
