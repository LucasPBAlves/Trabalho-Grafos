from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QListWidget,
                             QMessageBox)
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState


class Screen3(QDialog):
    backSignal = pyqtSignal()
    nextSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Criação e remoção de arestas")
        self.setGeometry(100, 100, 600, 400)
        self.edges = []  # Lista para armazenar as arestas
        self.uniqueVertices = set()  # Conjunto para armazenar vértices únicos
        self.vertices = SharedState.getVerticesCount()  # Total de vértices permitidos
        self.isDirected = SharedState.getIsDirected()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Criação e remoção de arestas", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.remainingVerticesLabel = QLabel(f"Vértices restantes: {self.vertices - len(self.uniqueVertices)}", self)
        self.remainingVerticesLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.remainingVerticesLabel)

        self.edgesList = QListWidget(self)
        layout.addWidget(self.edgesList)

        inputLayout = QHBoxLayout()
        self.vertex1Input = QLineEdit(self)
        self.vertex1Input.setPlaceholderText("Vértice 1")
        inputLayout.addWidget(self.vertex1Input)

        self.vertex2Input = QLineEdit(self)
        self.vertex2Input.setPlaceholderText("Vértice 2")
        inputLayout.addWidget(self.vertex2Input)

        layout.addLayout(inputLayout)

        addEdgeButton = QPushButton("Adicionar Aresta", self)
        addEdgeButton.clicked.connect(self.addEdge)
        layout.addWidget(addEdgeButton)

        removeEdgeButton = QPushButton("Remover Aresta Selecionada", self)
        removeEdgeButton.clicked.connect(self.removeSelectedEdge)
        layout.addWidget(removeEdgeButton)

        navButtonsLayout = QHBoxLayout()
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        navButtonsLayout.addWidget(backButton)

        self.nextButton = QPushButton("Próximo", self)
        self.nextButton.clicked.connect(self.nextSignal.emit)
        self.nextButton.setEnabled(False)
        navButtonsLayout.addWidget(self.nextButton)

        layout.addLayout(navButtonsLayout)
        self.setLayout(layout)

    def addEdge(self):
        v1 = self.vertex1Input.text().strip()
        v2 = self.vertex2Input.text().strip()
        if not v1 or not v2:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, insira ambos os vértices para a aresta.")
            return
        edge = f"{v1}->{v2}" if self.isDirected or v1 <= v2 else f"{v2}->{v1}"
        if edge in self.edges or (not self.isDirected and f"{v2}->{v1}" in self.edges):
            QMessageBox.warning(self, "Aresta Duplicada", "Esta aresta já foi adicionada ou é inválida.")
            return

        self.edges.append(edge)
        self.edgesList.addItem(edge)
        self.uniqueVertices.update([v1, v2])
        self.remainingVerticesLabel.setText(f"Vértices restantes: {self.vertices - len(self.uniqueVertices)}")
        self.vertex1Input.clear()
        self.vertex2Input.clear()
        self.checkIfComplete()

    def removeSelectedEdge(self):
        selectedItems = self.edgesList.selectedItems()
        if not selectedItems:
            return
        for item in selectedItems:
            edge = item.text()
            v1, v2 = edge.split("->")
            self.edges.remove(edge)
            self.edgesList.takeItem(self.edgesList.row(item))
            # Atualiza os vértices únicos após a remoção
            self.updateUniqueVerticesAfterRemoval(v1, v2)
        self.remainingVerticesLabel.setText(f"Vértices restantes: {self.vertices - len(self.uniqueVertices)}")
        self.checkIfComplete()

    def updateUniqueVerticesAfterRemoval(self, v1, v2):
        # Atualizar a lista de vértices únicos após a remoção de uma aresta
        for vertex in [v1, v2]:
            if all(vertex not in edge.split("->") for edge in self.edges):
                self.uniqueVertices.discard(vertex)

    def checkIfComplete(self):
        # Habilita o botão Próximo apenas se todos os vértices únicos foram adicionados
        self.nextButton.setEnabled(len(self.uniqueVertices) == self.vertices)

