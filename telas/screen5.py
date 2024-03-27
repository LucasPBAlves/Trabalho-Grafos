from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt
from shared_state import SharedState  # Importação hipotética do estado compartilhado

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
        self.vertice_input.setPlaceholderText("Insira o vértice")
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

    def identificar_vizinhos(self):
        vertice = self.vertice_input.text().strip()
        if not vertice:
            QMessageBox.warning(self, "Erro", "Por favor, insira o vértice para identificação.")
            return

        # Acesso à lista de arestas armazenada em SharedState
        arestas = SharedState.get_arestas()  # Método hipotético para obter as arestas

        # Calcular vizinhança para grafo não direcionado
        vizinhanca = set()
        for aresta in arestas:
            v1, v2 = aresta.split("->")
            if v1 == vertice:
                vizinhanca.add(v2)
            elif v2 == vertice:
                vizinhanca.add(v1)

        # Exibir a lista de vizinhos em uma caixa de diálogo
        QMessageBox.information(self, "Vizinhos", f"Os vizinhos do vértice {vertice} são: {', '.join(vizinhanca)}")
