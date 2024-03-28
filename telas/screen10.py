from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QMessageBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState
import itertools

class Screen10(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o grafo é completo")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Adiciona espaçador no topo para padding vertical
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.label = QLabel("Clique para verificar se o grafo é completo.", self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.label)

        # Layout horizontal para centralizar o botão de verificar
        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))  # Espaçador esquerdo

        checkButton = QPushButton("Verificar", self)
        checkButton.clicked.connect(self.checkIfGraphIsComplete)
        buttonLayout.addWidget(checkButton)

        buttonLayout.addItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))  # Espaçador direito

        layout.addLayout(buttonLayout)

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton)

        # Adiciona espaçador no final para padding vertical
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        self.setLayout(layout)

    def checkIfGraphIsComplete(self):
        arestas_str = SharedState.get_aresta()
        if not arestas_str:
            QMessageBox.warning(self, "Aviso", "Não há arestas definidas no grafo.")
            return

        arestas = arestas_str.split(';')
        vertices = set()
        for aresta in arestas:
            v1, v2 = aresta.split('-')
            vertices.add(v1)
            vertices.add(v2)

        is_complete = True
        for v1, v2 in itertools.combinations(vertices, 2):
            if f"{v1}-{v2}" not in arestas and f"{v2}-{v1}" not in arestas:
                is_complete = False
                break

        if is_complete:
            self.label.setText("O grafo é completo.")
        else:
            self.label.setText("O grafo não é completo.")

if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen10()
    screen.show()
    sys.exit(app.exec())
