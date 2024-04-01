import itertools

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QMessageBox

from shared_state import SharedState


class Screen10(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o grafo é completo")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        instructionLabel = QLabel("Clique para verificar se o grafo é completo.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        checkButton = QPushButton("Verificar", self)
        checkButton.setMaximumWidth(200)
        checkButton.clicked.connect(self.checkIfGraphIsComplete)
        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        buttonLayout.addWidget(checkButton)
        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButtonLayout = QHBoxLayout()
        backButtonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding,
                                             QSizePolicy.Policy.Minimum))
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        backButtonLayout.addWidget(backButton)
        layout.addLayout(backButtonLayout)

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
            self.resultLabel.setText("O grafo é completo.")
        else:
            self.resultLabel.setText("O grafo não é completo.")
