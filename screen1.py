from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal

class Screen1(QDialog):
    backSignal = pyqtSignal()
    nextSignal = pyqtSignal()  # Adicionado o sinal para navegação para a próxima tela

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Criação de um grafo com X vértices")
        self.setGeometry(100, 100, 600, 400)
        self.vertices = 0
        self.graph_representation = []
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Insira o número de vértices do grafo:", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.verticesInput = QLineEdit(self)
        self.verticesInput.setPlaceholderText("Número de vértices")
        layout.addWidget(self.verticesInput)

        addVerticesButton = QPushButton("Adicionar Vértices", self)
        addVerticesButton.clicked.connect(self.createGraph)
        layout.addWidget(addVerticesButton)

        self.statusMessage = QLabel("", self)
        self.statusMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.statusMessage)

        buttonsLayout = QHBoxLayout()

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        buttonsLayout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignLeft)

        self.nextButton = QPushButton("Próximo", self)
        self.nextButton.clicked.connect(self.nextSignal.emit)
        self.nextButton.setEnabled(False)
        buttonsLayout.addWidget(self.nextButton, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addLayout(buttonsLayout)
        self.setLayout(layout)

    def createGraph(self):
        try:
            self.vertices = int(self.verticesInput.text())
            if self.vertices > 0:
                self.graph_representation = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]
                self.statusMessage.setText(f"Grafo criado com {self.vertices} vértices.")
                self.nextButton.setEnabled(True)
            else:
                self.statusMessage.setText("Por favor, insira um número positivo de vértices.")
                self.nextButton.setEnabled(False)
        except ValueError:
            self.statusMessage.setText("Por favor, insira um número válido de vértices.")
            self.nextButton.setEnabled(False)
