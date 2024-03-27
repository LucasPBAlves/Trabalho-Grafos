from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QMessageBox)
from PyQt6.QtCore import Qt, pyqtSignal
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
        print("tela 6")
        label = QLabel("Identificação dos Sucessores e Predecessores de um Vértice", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Campo de entrada para o vértice de interesse
        self.vertexInput = QLineEdit(self)
        self.vertexInput.setPlaceholderText("Insira o vértice")
        layout.addWidget(self.vertexInput)

        # Botão para identificar sucessores e predecessores
        identifyButton = QPushButton("Identificar Sucessores e Predecessores", self)
        identifyButton.clicked.connect(self.identifySuccessorsPredecessors)
        layout.addWidget(identifyButton)

        # Área para exibir sucessores
        self.successorsLabel = QLabel("", self)
        self.successorsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.successorsLabel)

        # Área para exibir predecessores
        self.predecessorsLabel = QLabel("", self)
        self.predecessorsLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.predecessorsLabel)

        # Botão Voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton)

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
            if '-' in aresta:
                v1, v2 = aresta.split('-')
                if v1 == vertex:
                    successors.add(v2)
                if v2 == vertex:
                    predecessors.add(v1)
        self.successorsLabel.setText(f"Sucessores de {vertex}: {', '.join(successors)}")
        self.predecessorsLabel.setText(f"Predecessores de {vertex}: {', '.join(predecessors)}")
