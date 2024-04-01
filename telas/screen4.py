from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QLabel

from shared_state import SharedState


class Screen4(QWidget):
    backSignal = pyqtSignal()
    actionSignal = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Menu de Operações")
        self.initUI()

    def initUI(self):
        mainLayout = QVBoxLayout(self)

        title = QLabel("Escolha a ação desejada:", self)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        mainLayout.addWidget(title)

        mainLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        isDirected = SharedState.get_is_directed()

        if not isDirected:
            self.addButton(mainLayout, "Identificação da vizinhança de um vértice", 5)
        if isDirected:
            self.addButton(mainLayout, "Identificação dos sucessores e predecessores de um vértice", 6)

        self.addButton(mainLayout, "Identificação do grau de um determinado vértice", 7)
        self.addButton(mainLayout, "Testar se o grafo é simples", 8)
        self.addButton(mainLayout, "Testar se o grafo é regular", 9)
        self.addButton(mainLayout, "Testar se o grafo é completo", 10)
        self.addButton(mainLayout, "Testar se o grafo é bipartido", 11)
        self.addButton(mainLayout, "Representação de grafos utilizando Matriz de Adjacência", 12)
        self.addButton(mainLayout, "Representação de grafos utilizando Lista de Adjacência", 13)

        mainLayout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButtonLayout = QHBoxLayout()
        backButtonLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        backButtonLayout.addWidget(backButton)
        mainLayout.addLayout(backButtonLayout)

    def addButton(self, layout, text, screen_id):
        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        button = QPushButton(text, self)
        button.setFixedSize(800, 40)
        button.clicked.connect(lambda: self.buttonClicked(screen_id))
        buttonLayout.addWidget(button)

        buttonLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

    def buttonClicked(self, screen_id):
        print("apertado 2")
        print(screen_id)
        self.actionSignal.emit(screen_id)
