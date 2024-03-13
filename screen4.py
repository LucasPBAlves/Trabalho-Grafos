from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from screen1 import Screen1


class Screen4(QDialog):
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

    def vizinhanca_vertice(self, vertice):

        vizinhanca = []
        self.screen1 = Screen1()
        for i in range(self.vertice):
            if self.screen1.graph_representation[vertice][i] == 1:
                vizinhanca.append(i)
        return vizinhanca

    def identificar_vizinhos(self):
        # Obter o vértice inserido pelo usuário
        vertice = self.vertice_input.text()

        # Verificar se o vértice inserido é um número inteiro
        try:
            vertice = int(vertice)
        except ValueError:
            QMessageBox.warning(self, "Erro", "Insira um número inteiro válido para o vértice.")
            return

        # Chamar o método de identificação de vizinhos da classe MatrizAdjacencia
        vizinhanca = self.vizinhanca_vertice(vertice)

        # Exibir a lista de vizinhos em uma caixa de diálogo
        QMessageBox.information(self, "Vizinhos", f"Os vizinhos do vértice {vertice} são: {vizinhanca}")
