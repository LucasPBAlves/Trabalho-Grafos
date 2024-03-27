from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from telas.screen3 import Screen3


class Screen5(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Identificação da vizinhança de um vértice")
        self.setGeometry(100, 100, 600, 400)  # Tamanho e posição da janela
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Título da tela
        label = QLabel("Identificação da vizinhança de um vértice", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Campo de entrada para o vértice desejado
        self.vertice_input = QLineEdit(self)
        layout.addWidget(self.vertice_input)

        # Botão para identificar os vizinhos
        vizinhosButton = QPushButton("Identificar Vizinhos", self)
        vizinhosButton.clicked.connect(self.identificar_vizinhos)
        layout.addWidget(vizinhosButton)

        # Botão Voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.close)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

   