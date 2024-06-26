from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QListWidget, QMessageBox

from shared_state import SharedState


class Screen3(QDialog):
    backSignal = pyqtSignal()
    nextSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Criação e Remoção de Arestas")
        self.setGeometry(100, 100, 600, 400)
        self.edges = []  # Lista para armazenar as arestas
        self.uniqueVertices = set()  # Conjunto para armazenar vértices únicos
        self.vertices = SharedState.get_vertices_count()  # Total de vértices permitidos
        self.isDirected = SharedState.get_is_directed()
        self.edgesString = ""  # String para salvar as arestas adicionadas
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        label = QLabel("Criação e Remoção de Arestas", self)
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

        self.weightInput = QLineEdit(self)
        self.weightInput.setPlaceholderText("Peso (Padrão: 1)")
        inputLayout.addWidget(self.weightInput)

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
        self.nextButton.clicked.connect(self.gotoNextScreen)
        self.nextButton.setEnabled(False)
        navButtonsLayout.addWidget(self.nextButton)

        layout.addLayout(navButtonsLayout)

    def addEdge(self):
        v1 = self.vertex1Input.text().strip()
        v2 = self.vertex2Input.text().strip()
        weight = self.weightInput.text().strip() or "1"  # Preencha com "1" se estiver vazio

        if not v1 or not v2:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, insira ambos os vértices para a aresta.")
            return

        edgeStringFormat = f"{v1}-{v2}-{weight}"
        edge = f"{v1}->{v2}" if self.isDirected or v1 <= v2 else f"{v2}->{v1}"

        if edge in self.edges or (not self.isDirected and f"{v2}->{v1}" in self.edges):
            QMessageBox.warning(self, "Aresta Duplicada", "Esta aresta já foi adicionada ou é inválida.")
            return

        self.edges.append(edge)
        self.edgesList.addItem(edge)
        self.uniqueVertices.update([v1, v2])
        self.edgesString += ";" + edgeStringFormat if self.edgesString else edgeStringFormat
        self.remainingVerticesLabel.setText(f"Vértices restantes: {self.vertices - len(self.uniqueVertices)}")
        self.vertex1Input.clear()
        self.vertex2Input.clear()
        self.weightInput.clear()
        self.checkIfComplete()

    def removeSelectedEdge(self):
        selectedItems = self.edgesList.selectedItems()
        if not selectedItems:
            return
        for item in selectedItems:
            edge = item.text()
            self.edges.remove(edge)
            self.edgesList.takeItem(self.edgesList.row(item))
            v1, v2 = edge.split("->")
            self.updateUniqueVerticesAfterRemoval(v1, v2)
        self.remainingVerticesLabel.setText(f"Vértices restantes: {self.vertices - len(self.uniqueVertices)}")
        self.checkIfComplete()

    def updateUniqueVerticesAfterRemoval(self, v1, v2):
        # Remove vértices de `self.uniqueVertices` se não estiverem mais em nenhuma aresta
        self.uniqueVertices = {v.split("->")[0] for v in self.edges}.union({v.split("->")[1] for v in self.edges})
        self.remainingVerticesLabel.setText(f"Vértices restantes: {self.vertices - len(self.uniqueVertices)}")

    def checkIfComplete(self):
        # Habilita o botão "Próximo" se o número de vértices únicos adicionados corresponder ao total de vértices permitidos
        self.nextButton.setEnabled(len(self.uniqueVertices) >= self.vertices)

    def gotoNextScreen(self):
        if self.nextButton.isEnabled():
            print(f"Edges string: {self.edgesString}")
            SharedState.set_aresta(self.edgesString)
            self.nextSignal.emit()
        else:
            QMessageBox.warning(self, "Ação Inválida", "Adicione todas as arestas necessárias antes de prosseguir.")
