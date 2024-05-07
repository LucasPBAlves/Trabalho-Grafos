from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QMessageBox,
                             QSpacerItem, QSizePolicy)

from shared_state import SharedState


class Screen6(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Identificação dos Sucessores e Predecessores")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Identificação dos Sucessores e Predecessores de um Vértice", self)
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

        identifyButton = QPushButton("Identificar", self)
        identifyButton.setFixedSize(200, 40)
        identifyButton.clicked.connect(self.identifySuccessorsPredecessors)
        buttonLayout.addWidget(identifyButton)

        buttonLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

        self.successorsLabel = QLabel("", self)
        self.successorsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.successorsLabel)

        self.predecessorsLabel = QLabel("", self)
        self.predecessorsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.predecessorsLabel)

        backButton = QPushButton("Voltar", self)
        backButton.setFixedSize(200, 40)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)
        backButton.clicked.connect(self.backSignal.emit)

        self.setLayout(layout)

    def identifySuccessorsPredecessors(self):
        vertex = self.vertexInput.text().strip()
        if not vertex:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, insira o vértice.")
            return

        arestas = SharedState.get_aresta()
        successors = set()
        predecessors = set()

        for aresta in arestas.split(';'):
            try:
                v1, v2, _ = aresta.split('-')
                if v1 == vertex:
                    successors.add(v2)
                if v2 == vertex:
                    predecessors.add(v1)
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{aresta}' não está no formato correto.")

        self.successorsLabel.setText(f"Sucessores de {vertex}: {', '.join(sorted(successors))}")
        self.predecessorsLabel.setText(f"Predecessores de {vertex}: {', '.join(sorted(predecessors))}")
