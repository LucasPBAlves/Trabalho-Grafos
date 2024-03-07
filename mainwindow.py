import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon

# Importações das telas
from screen1 import Screen1
from screen2 import Screen2
from screen3 import Screen3
# Adicione imports adicionais para Screen4 até Screen12 conforme necessário

from styles import DARK_THEME_STYLE

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Grafos')
        self.setGeometry(350, 100, 1280, 720)
        self.setStyleSheet(DARK_THEME_STYLE)
        self.setWindowIcon(QIcon('assets/graph.ico'))

        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.setup_initial_screen()
        self.setup_screen1()
        self.setup_screen2()
        self.setup_screen3()
        # Continue a adicionar as telas conforme necessário

    def setup_initial_screen(self):
        initial_widget = QWidget()
        layout = QVBoxLayout(initial_widget)

        title = QLabel('Implementação de Grafos', initial_widget)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24pt; font-weight: bold; font-family: Arial;")
        layout.addWidget(title)

        layout.addItem(QSpacerItem(15, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        manip_subtitle = QLabel('Escolha uma opção:', initial_widget)
        manip_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(manip_subtitle)

        # Botões centralizados
        buttons_layout = QVBoxLayout()
        create_graph_button = QPushButton("Criação de um grafo com X vértices", initial_widget)
        create_graph_button.clicked.connect(lambda: self.goto_screen(1))
        create_graph_button.setMinimumHeight(40)
        create_graph_button.setMaximumWidth(400)
        buttons_layout.addWidget(create_graph_button)

        use_predefined_graph_button = QPushButton("Usar grafos já plotados", initial_widget)
        use_predefined_graph_button.clicked.connect(self.not_implemented_yet)
        use_predefined_graph_button.setMinimumHeight(40)
        use_predefined_graph_button.setMaximumWidth(400)
        buttons_layout.addWidget(use_predefined_graph_button)

        h_layout = QHBoxLayout()
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        h_layout.addLayout(buttons_layout)
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(h_layout)

        self.stackedWidget.addWidget(initial_widget)

    def setup_screen1(self):
        self.screen1 = Screen1()
        self.screen1.nextSignal.connect(lambda: self.goto_screen(2))
        self.stackedWidget.addWidget(self.screen1)

    # Dentro de MainWindow.py
    def setup_screen2(self):
        self.screen2 = Screen2()
        self.screen2.nextSignal.connect(
            lambda: self.goto_screen(3))  # Isso requer que 'goto_screen' possa lidar com índices
        self.stackedWidget.addWidget(self.screen2)

    def setup_screen3(self):
        self.screen3 = Screen3()
        self.screen3.backSignal.connect(lambda: self.goto_screen(2))  # Exemplo para voltar à Screen2
        self.screen3.nextSignal.connect(lambda: self.goto_screen(4))  # Exemplo para ir à Screen4, se aplicável
        self.stackedWidget.addWidget(self.screen3)

    # Métodos setup_screen4() até setup_screen12() conforme necessário

    def goto_screen(self, screen_index):
        self.stackedWidget.setCurrentIndex(screen_index)

    def not_implemented_yet(self):
        print("Função não implementada")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
