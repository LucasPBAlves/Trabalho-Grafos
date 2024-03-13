# screen9.py
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt

from screen1 import Screen1


class Screen9(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o grafo é completo")
        self.setGeometry(100, 100, 600, 400)  # Tamanho e posição da janela
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Exemplo de um widget adicional, pode ser um texto ou qualquer coisa relacionada a esta tela
        label = QLabel("Testar se o grafo é completo", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Botão Voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.close)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    def is_completo(self):
        self.screen1 = Screen1()
        for i in range(self.vertice):
            for j in range(self.vertice):
                if i != j and self.screen1.graph_representation[i][j] != 1:
                    return False
        return True
