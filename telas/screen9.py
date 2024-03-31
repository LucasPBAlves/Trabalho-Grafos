from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QMessageBox, QHBoxLayout, QSpacerItem, \
    QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
from collections import defaultdict
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

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))  # Espaço no topo

        label = QLabel("Clique para testar se o grafo é regular:", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        # Espaço entre o label e o botão
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))  # Espaço antes do botão

        testButton = QPushButton("Testar Regularidade", self)
        testButton.setFixedSize(200, 40)  # Ajusta tamanho do botão
        testButton.clicked.connect(self.testRegularity)
        buttonLayout.addWidget(testButton)

        buttonLayout.addItem(
            QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))  # Espaço após o botão
        layout.addLayout(buttonLayout)

        # Espaço entre o botão e o resultado
        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        # Espaço antes do botão "Voltar"
        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButton = QPushButton("Voltar", self)
        backButton.setFixedSize(200, 40)  # Ajusta tamanho do botão "Voltar"
        backButtonLayout = QHBoxLayout()
        backButtonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                                             QSizePolicy.Policy.Minimum))  # Preenche o espaço até o botão "Voltar"
        backButtonLayout.addWidget(backButton)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addLayout(backButtonLayout)

        self.setLayout(layout)

    def testRegularity(self):
        arestas = SharedState.get_aresta().split(';')
        grau_vertices = defaultdict(int)

        for aresta in arestas:
            v1, v2 = aresta.split('-')
            grau_vertices[v1] += 1
            grau_vertices[v2] += 1

        graus = set(grau_vertices.values())

        if len(graus) == 1:
            self.resultLabel.setText(f"O grafo é regular com grau {graus.pop()}.")
        else:
            self.resultLabel.setText("O grafo não é regular.")
