# screen12.py
from tkinter import messagebox
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState

class Screen13(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Representação de grafos utilizando Lista de Adjacência")
        self.setGeometry(100, 100, 600, 400)  # Tamanho e posição da janela
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        instructionLabel = QLabel("Clique no botão abaixo para mostrar a Lista de adjacência do grafo.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)
         # Layout horizontal para centralizar o botão
        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        testButton = QPushButton("Mostrar Lista de Adjacência", self)
        testButton.clicked.connect(self.showAdjacencyList)
        buttonLayout.addWidget(testButton)

        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

         # Label para exibir a matriz de adjacência
        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)
        # Padding no fundo
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Botão Voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.close)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    def showAdjacencyList(self):
            arestas_str = SharedState.get_aresta()
            if not arestas_str:
                messagebox.information(self, "Aviso!", "Nenhuma aresta foi cadastrada.")
                return

            isDirected = SharedState.get_is_directed()
            arestas = arestas_str.split(";")
            vertices= {}


            for aresta in arestas:
                v1, v2 = aresta.split('-')
                if v1 not in vertices:
                    vertices[v1] = []
                if v2 not in vertices:
                    vertices[v2] = []

                vertices[v1].append(v2)
                if not isDirected:

                 vertices[v2].append(v1)

                adjacencylist_str = ""

                for vertex, adj_list in vertices.items():
                    if isDirected:
                        adjacencylist_str += f"{vertex} -> {', '.join(adj_list)}\n"
                    else:
                        adjacencylist_str += f"{vertex} -> {','.join(adj_list)} \n"

            self.resultLabel.setText(adjacencylist_str)
                        
                