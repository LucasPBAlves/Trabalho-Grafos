from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState


class Screen11(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o grafo é bipartido")
        self.setGeometry(100, 100, 600, 400)
        self.resultLabel = QLabel("", self)  # Label para mostrar o resultado
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Padding no topo
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        instructionLabel = QLabel("Clique no botão abaixo para testar se o grafo é bipartido.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        # Botão de teste centralizado
        testButton = QPushButton("Testar", self)
        testButton.clicked.connect(self.testIfGraphIsBipartite)
        layout.addWidget(testButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Espaço antes do resultado
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))

        # Configurações do label de resultado
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        # Padding no fundo
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    def testIfGraphIsBipartite(self):
        # Implementação fictícia do teste bipartido. Substitua com seu algoritmo real
        is_bipartite = self.isGraphBipartite()

        # Exibir resultado diretamente na tela
        if is_bipartite:
            self.resultLabel.setText("O grafo é bipartido.")
        else:
            self.resultLabel.setText("O grafo não é bipartido.")

    def isGraphBipartite(self):
        # Aqui, você implementaria a lógica real para verificar se o grafo é bipartido
        # Essa função deve retornar True se o grafo for bipartido e False caso contrário
        return True  # Retorna True apenas para exemplo


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen11()
    screen.show()
    sys.exit(app.exec())
