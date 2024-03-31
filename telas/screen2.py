from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout

from shared_state import SharedState


class Screen2(QDialog):
    backSignal = pyqtSignal()
    nextSignal = pyqtSignal()

    def __init__(self, parent=None):
        print("Tela2")
        super().__init__(parent)
        self.setWindowTitle("Definição do tipo de grafo")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        print("tela2")
        layout = QVBoxLayout()

        titleLabel = QLabel("Definição do tipo de grafo", self)
        titleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titleLabel.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        layout.addWidget(titleLabel)

        infoLabel = QLabel("Escolha se o grafo é direcionado ou não direcionado:", self)
        infoLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        infoLabel.setFont(QFont("Arial", 14))
        layout.addWidget(infoLabel)

        buttonContainer = QHBoxLayout()
        buttonContainer.setAlignment(Qt.AlignmentFlag.AlignCenter)

        selectionLayout = QVBoxLayout()
        directedButton = QPushButton("Direcionado", self)
        undirectedButton = QPushButton("Não Direcionado", self)

        directedButton.setFixedSize(200, 40)
        undirectedButton.setFixedSize(200, 40)

        directedButton.clicked.connect(lambda: self.setGraphType(True))
        undirectedButton.clicked.connect(lambda: self.setGraphType(False))

        selectionLayout.addWidget(directedButton)
        selectionLayout.addWidget(undirectedButton)
        selectionLayout.setSpacing(10)

        buttonContainer.addLayout(selectionLayout)
        layout.addLayout(buttonContainer)

        self.choiceLabel = QLabel("", self)
        self.choiceLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.choiceLabel)

        navButtonsLayout = QHBoxLayout()
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        navButtonsLayout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignLeft)

        self.nextButton = QPushButton("Próximo", self)
        self.nextButton.clicked.connect(self.gotoNextScreen)
        self.nextButton.setEnabled(False)
        navButtonsLayout.addWidget(self.nextButton, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addLayout(navButtonsLayout)
        self.setLayout(layout)

    def setGraphType(self, isDirected):
        SharedState.set_is_directed(isDirected)
        self.nextButton.setEnabled(True)
        choiceText = "Tipo de grafo selecionado: Direcionado" if isDirected else "Tipo de grafo selecionado: Não Direcionado"
        self.choiceLabel.setText(choiceText)

    def gotoNextScreen(self):
        if SharedState.get_is_directed() is not None:
            print(SharedState.is_directed)
            self.nextSignal.emit()
        else:
            self.choiceLabel.setText("Por favor, selecione um tipo de grafo para continuar.")
