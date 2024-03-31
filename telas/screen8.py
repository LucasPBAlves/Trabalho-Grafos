from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState


class Screen8(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o grafo é simples")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Espaçamento no topo
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        instructionLabel = QLabel("Clique no botão abaixo para testar se o grafo é simples.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        # Espaçador entre o texto de instrução e o botão
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Botão centralizado para testar se o grafo é simples
        testButton = QPushButton("Testar", self)
        testButton.setFixedSize(200, 40)
        layout.addWidget(testButton, alignment=Qt.AlignmentFlag.AlignCenter)
        testButton.clicked.connect(self.testIfGraphIsSimple)

        # Espaçador entre o botão e a área de resultado
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        # Área para exibir se é simples ou não
        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        # Espaçamento antes do botão Voltar
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButton = QPushButton("Voltar", self)
        backButton.setFixedSize(200, 40)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)
        backButton.clicked.connect(self.backSignal.emit)

        self.setLayout(layout)

    def testIfGraphIsSimple(self):
        arestas_str = SharedState.get_aresta()
        if not arestas_str:
            QMessageBox.warning(self, "Aviso", "Não há arestas definidas no grafo.")
            return

        arestas = arestas_str.split(';')
        vertices = set()
        simple = True
        for aresta in arestas:
            v1, v2 = aresta.split('-')
            if v1 == v2:  # Detecta um laço
                simple = False
                break
            if arestas.count(aresta) > 1:  # Detecta arestas paralelas
                simple = False
                break
            vertices.add(frozenset([v1, v2]))

        if len(vertices) != len(arestas):  # Detecta arestas paralelas de forma indireta
            simple = False

        if simple:
            self.resultLabel.setText("O grafo é simples.")
        else:
            self.resultLabel.setText("O grafo não é simples.")


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen8()
    screen.show()
    sys.exit(app.exec())
