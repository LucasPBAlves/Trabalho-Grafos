from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt, pyqtSignal

class Screen3(QDialog):
    backSignal = pyqtSignal()  # Adicionando sinal para a ação de voltar
    nextSignal = pyqtSignal()  # Adicionando sinal para a ação de ir para a próxima tela, se necessário

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Criação e remoção de arestas")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Criação e remoção de arestas", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Botão Próximo, se necessário
        nextButton = QPushButton("Próximo", self)  # Use apenas se você precisar de navegação para frente
        nextButton.clicked.connect(self.nextSignal.emit)  # Conecta o botão a emitir nextSignal quando clicado
        layout.addWidget(nextButton, alignment=Qt.AlignmentFlag.AlignRight)

        # Botão Voltar
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)  # Agora emite backSignal em vez de fechar a janela
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignLeft)

        self.setLayout(layout)
