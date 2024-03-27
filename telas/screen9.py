# screen8.py
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from telas.screen6 import Screen6


class Screen9(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o grafo é regular")
        self.setGeometry(100, 100, 600, 400)  # Tamanho e posição da janela
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Exemplo de um widget adicional, pode ser um texto ou qualquer coisa relacionada a esta tela
        label = QLabel("Testar se o grafo é regular", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Botão Voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.close)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    def is_regular(self):
        self.screen6 = Screen6()
        grau_base = self.screen6.grau_vertice(0)
        for i in range(1, self.vertice):
            if self.screen6.grau_vertice(i) != grau_base:
                return False
        return True
