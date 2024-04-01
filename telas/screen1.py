from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QHBoxLayout, QSpacerItem, QSizePolicy

from shared_state import SharedState


class Screen1(QDialog):
    backSignal = pyqtSignal()
    nextSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Criação de um grafo com X vértices")
        self.setGeometry(100, 100, 600, 400)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel("Insira o número de vértices do grafo:", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        inputLayout = QHBoxLayout()
        inputLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.verticesInput = QLineEdit(self)
        self.verticesInput.setPlaceholderText("Número de vértices")
        self.verticesInput.setFixedSize(200, 40)
        inputLayout.addWidget(self.verticesInput)
        inputLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(inputLayout)

        buttonLayout = QHBoxLayout()
        buttonLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        add_vertices_button = QPushButton("Adicionar Vértices", self)
        add_vertices_button.clicked.connect(self.create_graph)
        add_vertices_button.setFixedSize(200, 40)
        buttonLayout.addWidget(add_vertices_button)
        buttonLayout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

        self.statusMessage = QLabel("", self)
        self.statusMessage.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.statusMessage)

        buttons_layout = QHBoxLayout()
        back_button = QPushButton("Voltar", self)
        back_button.clicked.connect(self.backSignal.emit)
        buttons_layout.addWidget(back_button, alignment=Qt.AlignmentFlag.AlignLeft)

        self.nextButton = QPushButton("Próximo", self)
        self.nextButton.clicked.connect(self.goto_next_screen)
        self.nextButton.setEnabled(False)
        buttons_layout.addWidget(self.nextButton, alignment=Qt.AlignmentFlag.AlignRight)

        layout.addLayout(buttons_layout)
        self.setLayout(layout)

    def create_graph(self):
        try:
            vertices = int(self.verticesInput.text())
            if vertices > 0:
                SharedState.set_vertices_count(vertices)
                self.statusMessage.setText(f"Grafo criado com {vertices} vértices.")
                self.nextButton.setEnabled(True)
            else:
                self.statusMessage.setText("Por favor, insira um número positivo de vértices.")
                self.nextButton.setEnabled(False)
        except ValueError:
            self.statusMessage.setText("Por favor, insira um número válido de vértices.")
            self.nextButton.setEnabled(False)

    def goto_next_screen(self):
        if SharedState.get_vertices_count() > 0:
            print(SharedState.vertices_count)
            self.nextSignal.emit()
        else:
            self.statusMessage.setText("Insira um valor válido (>0) de vértices para continuar.")
