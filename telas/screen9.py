from collections import defaultdict
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, \
    QSizePolicy, QMessageBox

from shared_state import SharedState

class Screen9(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o Grafo é Regular")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        label = QLabel("Clique para testar se o grafo é regular:", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        testButton = QPushButton("Testar Regularidade", self)
        testButton.setFixedSize(200, 40)
        testButton.clicked.connect(self.testRegularity)
        buttonLayout.addWidget(testButton)

        buttonLayout.addItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButton = QPushButton("Voltar", self)
        backButton.setFixedSize(200, 40)
        backButtonLayout = QHBoxLayout()
        backButtonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                                             QSizePolicy.Policy.Minimum))
        backButtonLayout.addWidget(backButton)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addLayout(backButtonLayout)

        self.setLayout(layout)

    def testRegularity(self):
        arestas_str = SharedState.get_aresta()
        if not arestas_str:
            QMessageBox.warning(self, "Aviso", "Não há arestas definidas no grafo.")
            return

        arestas = arestas_str.split(';')
        grau_vertices = defaultdict(int)

        for aresta in arestas:
            try:
                v1, v2, _ = aresta.split('-')
                grau_vertices[v1] += 1
                grau_vertices[v2] += 1
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{aresta}' não está no formato correto.")

        graus = set(grau_vertices.values())

        if len(graus) == 1:
            self.resultLabel.setText(f"O grafo é regular com grau {graus.pop()}.")
        else:
            self.resultLabel.setText("O grafo não é regular.")

if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen9()
    screen.show()
    sys.exit(app.exec())
