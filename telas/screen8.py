from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, \
    QMessageBox

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

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        instructionLabel = QLabel("Clique no botão abaixo para testar se o grafo é simples.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        testButton = QPushButton("Testar", self)
        testButton.setFixedSize(200, 40)
        layout.addWidget(testButton, alignment=Qt.AlignmentFlag.AlignCenter)
        testButton.clicked.connect(self.testIfGraphIsSimple)

        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

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
        arestas_set = set()
        simple = True

        for aresta in arestas:
            try:
                v1, v2, _ = aresta.split('-')
                if v1 == v2:  # Detecta um laço
                    simple = False
                    break

                # Usamos um conjunto imutável para representar uma aresta não orientada
                aresta_conjunto = frozenset([v1, v2])
                if aresta_conjunto in arestas_set:
                    simple = False
                    break

                arestas_set.add(aresta_conjunto)
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{aresta}' não está no formato correto.")

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
