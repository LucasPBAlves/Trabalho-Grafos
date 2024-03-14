from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QPushButton)
from PyQt6.QtCore import pyqtSignal
from shared_state import SharedState

class Screen4(QWidget):
    backSignal = pyqtSignal()
    actionSignal = pyqtSignal(str)  # sinal para a ação dos botões

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Menu de Operações")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        # Condicionalmente adicionar botões com base no tipo de grafo
        isDirected = SharedState.get_is_directed()

        if not isDirected:
            self.addButton(layout, "Identificação da vizinhança de um vértice",)
        if isDirected:
            self.addButton(layout, "Identificação dos sucessores e predecessores de um vértice")

        # Botões que aparecem independentemente do tipo de grafo
        self.addButton(layout, "Identificação do grau de um determinado vértice")
        self.addButton(layout, "Testar se o grafo é simples")
        self.addButton(layout, "Testar se o grafo é regular")
        self.addButton(layout, "Testar se o grafo é completo")
        self.addButton(layout, "Testar se o grafo é bipartido")
        self.addButton(layout, "Representação de grafos utilizando Matriz de Adjacência")
        self.addButton(layout, "Representação de grafos utilizando Lista de Adjacência")

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton)

    def addButton(self, layout, text):
        button = QPushButton(text, self)
        button.clicked.connect(lambda checked, b=text: self.buttonClicked(b))
        layout.addWidget(button)

    def buttonClicked(self, buttonText):
        self.actionSignal.emit(buttonText)
