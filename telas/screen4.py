from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton
from PyQt6.QtCore import pyqtSignal
from shared_state import SharedState

class Screen4(QWidget):
    backSignal = pyqtSignal()
    nextSignal = pyqtSignal()
    # Modificado para emitir um inteiro correspondente ao screen_id
    openScreenSignal = pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Menu de Operações")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)
        isDirected = SharedState.get_is_directed()

        # Aqui nós adicionamos diretamente o botão com sua ação correspondente
        if not isDirected:
            self.addButton(layout, "Identificação da vizinhança de um vértice", 5)
        if isDirected:
            self.addButton(layout, "Identificação dos sucessores e predecessores de um vértice", 6)

        self.addButton(layout, "Identificação do grau de um determinado vértice", 7)
        self.addButton(layout, "Testar se o grafo é simples", 8)
        self.addButton(layout, "Testar se o grafo é regular", 9)
        self.addButton(layout, "Testar se o grafo é completo", 10)
        self.addButton(layout, "Testar se o grafo é bipartido", 11)
        self.addButton(layout, "Representação de grafos utilizando Matriz de Adjacência", 12)
        self.addButton(layout, "Representação de grafos utilizando Lista de Adjacência", 13)

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton)

    def addButton(self, layout, text, screen_id):
        button = QPushButton(text, self)
        # Conecta diretamente o botão ao slot correto, emitindo o screen_id
        button.clicked.connect(lambda: self.buttonClicked(screen_id))
        print("apertado")
        layout.addWidget(button)

    def buttonClicked(self, screen_id):
        print("apertado 2")
        print(screen_id)
        # Emite o sinal com o screen_id ao ser clicado
        self.nextSignal.emit(screen_id)
