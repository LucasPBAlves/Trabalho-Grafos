from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QSpacerItem, QSizePolicy, QHBoxLayout
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

        inputLayout = QHBoxLayout()
        inputLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        self.vertexInput = QLineEdit(self)
        self.vertexInput.setPlaceholderText("Vértice")
        self.vertexInput.setFixedSize(200, 40)
        inputLayout.addWidget(self.vertexInput)

        inputLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(inputLayout)

        buttonLayout = QHBoxLayout()
        buttonLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        checkDegreeButton = QPushButton("Verificar Grau", self)
        checkDegreeButton.setFixedSize(200, 40)
        checkDegreeButton.clicked.connect(self.checkDegree)
        buttonLayout.addWidget(checkDegreeButton)

        buttonLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

        self.degreeLabel = QLabel("", self)
        self.degreeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.degreeLabel)

        backButton = QPushButton("Voltar", self)
        backButton.setFixedSize(200, 40)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)
        backButton.clicked.connect(self.backSignal.emit)

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
            try:
                v1, v2, _ = aresta.split('-')
                if vertex == v1:
                    degree += 1
                if not isDirected and vertex == v2:
                    degree += 1
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{aresta}' não está no formato correto.")

        self.degreeLabel.setText(f"O grau do vértice {vertex} é: {degree}")
