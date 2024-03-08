from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QApplication
from PyQt6.QtCore import Qt, pyqtSignal


class Screen1(QDialog):
    backSignal = pyqtSignal()
    nextSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.graph_representation = None
        self.nextButton = None
        self.statusMessage = None
        self.verticesInput = None
        self.setWindowTitle("Criação de um grafo com X vértices")
        self.setGeometry(100, 100, 600, 400)
        self.vertices = 0  # Inicializa o contador de vértices
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Insira o número de vértices do grafo:", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        self.verticesInput = QLineEdit(self)
        self.verticesInput.setPlaceholderText("Número de vértices")
        layout.addWidget(self.verticesInput)

        add_vertices_button = QPushButton("Adicionar Vértices", self)
        add_vertices_button.clicked.connect(self.create_graph)
        layout.addWidget(add_vertices_button)

        self.statusMessage = QLabel("", self)
        self.statusMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.statusMessage)

        buttons_layout = QHBoxLayout()

        back_button = QPushButton("Voltar", self)
        back_button.clicked.connect(self.backSignal.emit)
        buttons_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)
        self.statusMessage.setText("Insira um valor válido (>0) de vértices para continuar.")
        self.nextButton = QPushButton("Próximo", self)
        self.nextButton.clicked.connect(self.goto_next_screen)
        self.nextButton.setEnabled(False)
        buttons_layout.addWidget(self.nextButton, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def create_graph(self):
        try:
            self.vertices = int(self.verticesInput.text())
            if self.vertices > 0:
                self.graph_representation = [[0 for _ in range(self.vertices)] for _ in range(self.vertices)]
                self.statusMessage.setText(f"Grafo criado com {self.vertices} vértices.")
                self.nextButton.setEnabled(True)
            else:
                self.statusMessage.setText("Por favor, insira um número positivo de vértices.")
                self.nextButton.setEnabled(False)
        except ValueError:
            self.statusMessage.setText("Por favor, insira um número válido de vértices.")
            self.nextButton.setEnabled(False)

    def goto_next_screen(self):
        if self.vertices > 0:
            self.nextSignal.emit()
        else:
            self.statusMessage.setText("Insira um valor válido (>0) de vértices para continuar.")
