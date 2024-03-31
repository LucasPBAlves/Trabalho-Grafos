from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox
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

        # Padding no topo
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        instructionLabel = QLabel("Clique no botão abaixo para testar se o grafo é simples.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        # Layout horizontal para centralizar o botão
        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        testButton = QPushButton("Testar", self)
        testButton.clicked.connect(self.testIfGraphIsSimple)
        buttonLayout.addWidget(testButton)

        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

        # Padding no fundo
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

         # Área para exibir se é simples ou não
        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)

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
