from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QMessageBox, QLineEdit
from PyQt6.QtCore import Qt

from telas.screen1 import Screen1


class Screen6(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Identificação dos sucessores e predecessores de um vértice")
        self.setGeometry(100, 100, 600, 400)  # Tamanho e posição da janela
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Título da tela
        label = QLabel("Identificação dos sucessores e predecessores de um vértice", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Campo de entrada para o vértice desejado
        self.vertice_input = QLineEdit(self)
        layout.addWidget(self.vertice_input)

        # Botão para identificar os sucessores e predecessores
        button = QPushButton("Identificar Sucessores e Predecessores", self)
        button.clicked.connect(self.identificar_sucessores_predecessores)
        layout.addWidget(button)

        # Botão Voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.close)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    def predecessor_sucessor(self):
        # Obter o vértice inserido pelo usuário
        vertice = self.vertice_input.text()

        # Verificar se o vértice inserido é um número inteiro
        try:
            vertice = int(vertice)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Insira um número inteiro válido para o vértice.")
            return

        # Chamar a função para identificar os sucessores e predecessores
        predecessores, sucessores = self.identificar_sucessores_predecessores(vertice)

        # Exibir os sucessores e predecessores em caixas de diálogo
        QMessageBox.information(self, "Predecessores", f"Os predecessores do vértice {vertice} são: {predecessores}")
        QMessageBox.information(self, "Sucessores", f"Os sucessores do vértice {vertice} são: {sucessores}")

    def identificar_sucessores_predecessores(self, vertice):
        predecessores = []
        sucessores = []
        self.screen1 = Screen1()
        # Verificar predecessores
        for i in range(self.vertice):
            if self.screen1.graph_representation[i][vertice] == 1:
                predecessores.append(i)

        # Verificar sucessores
        for j in range(self.vertice):
            if self.vertice[vertice][j] == 1:
                sucessores.append(j)

        return predecessores, sucessores
