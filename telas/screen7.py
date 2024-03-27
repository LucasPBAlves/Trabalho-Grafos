from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState


class Screen7(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Identificação do Grau de um Vértice")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        label = QLabel("Insira o vértice para identificar o seu grau:", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.vertexInput = QLineEdit(self)
        self.vertexInput.setPlaceholderText("Vértice")
        layout.addWidget(self.vertexInput)

        checkDegreeButton = QPushButton("Verificar Grau", self)
        checkDegreeButton.clicked.connect(self.checkDegree)
        layout.addWidget(checkDegreeButton)

        self.degreeLabel = QLabel("", self)
        self.degreeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.degreeLabel)

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    def checkDegree(self):
        vertex = self.vertexInput.text().strip()
        if not vertex:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, insira um vértice.")
            return

        arestas = SharedState.get_aresta().split(';')
        isDirected = SharedState.get_is_directed()
        degree = 0

        for aresta in arestas:
            if isDirected:
                if '->' in aresta:
                    v1, v2 = aresta.split('->')
                    if vertex in (v1, v2):
                        degree += 1
            else:
                if '-' in aresta:
                    v1, v2 = aresta.split('-')
                    if vertex in (v1, v2):
                        degree += 1

        self.degreeLabel.setText(f"O grau do vértice {vertex} é: {degree}")

