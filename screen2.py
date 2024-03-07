from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt, pyqtSignal

class Screen2(QDialog):
    nextSignal = pyqtSignal()  # Corrigindo a definição do sinal

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Definição do tipo de grafo")
        self.setGeometry(100, 100, 600, 400)  # Tamanho e posição da janela
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Definição do tipo de grafo", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Potencialmente, um botão "Próximo"
        nextButton = QPushButton("Próximo", self)
        nextButton.clicked.connect(self.nextSignal.emit)  # Emitir nextSignal quando clicado
        layout.addWidget(nextButton, alignment=Qt.AlignmentFlag.AlignRight)

        # Botão Voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.close)  # Potencialmente, alterar para emitir um sinal de volta
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)
