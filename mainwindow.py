import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, \
    QSizePolicy, QHBoxLayout, QStackedWidget
from styles import DARK_THEME_STYLE

# Importações das telas
from telas.screen1 import Screen1
from telas.screen2 import Screen2
from telas.screen3 import Screen3
from telas.screen4 import Screen4
from telas.screen5 import Screen5


def not_implemented_yet():
    print("Função não implementada")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.stackedWidget = None
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Grafos')
        self.setGeometry(350, 100, 1280, 720)
        self.setStyleSheet(DARK_THEME_STYLE)
        self.setWindowIcon(QIcon('assets/graph.ico'))

        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.setup_initial_screen()
        self.setup_screen1()
        self.setup_screen2()
        # Screen3 será configurada sob demanda

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

        buttons_layout = QVBoxLayout()
        create_graph_button = QPushButton("Criação de um grafo com X vértices", initial_widget)
        create_graph_button.clicked.connect(lambda: self.goto_screen(1))
        create_graph_button.setMinimumHeight(40)
        create_graph_button.setMaximumWidth(400)
        buttons_layout.addWidget(create_graph_button)

        use_predefined_graph_button = QPushButton("Usar grafos já plotados", initial_widget)
        use_predefined_graph_button.clicked.connect(not_implemented_yet)
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

    def setup_screen2(self):
        self.screen2 = Screen2()
        self.screen2.nextSignal.connect(self.prepare_screen3)
        self.screen2.backSignal.connect(lambda: self.goto_screen(1))
        self.stackedWidget.addWidget(self.screen2)

    def prepare_screen3(self):
        if not hasattr(self, 'screen3'):
            self.screen3 = Screen3()
            self.screen3.backSignal.connect(lambda: self.goto_screen(self.stackedWidget.indexOf(self.screen2)))
            self.screen3.nextSignal.connect(self.prepare_screen4)
            self.stackedWidget.addWidget(self.screen3)
            self.stackedWidget.setCurrentWidget(self.screen3)

    def prepare_screen4(self):
        if not hasattr(self, 'screen4'):
            self.screen4 = Screen4()
            self.screen4.backSignal.connect(lambda: self.goto_screen(self.stackedWidget.indexOf(self.screen3)))
            self.stackedWidget.addWidget(self.screen4)
            self.screen4.nextSignal.connect(self.prepare_menu)
            self.stackedWidget.setCurrentWidget(self.screen4)

    def prepare_menu(self, screen_id):
        print(screen_id)
        # Aqui você prepara e exibe a tela correspondente ao ID recebido
        if screen_id == 5:
            if not hasattr(self, 'screen5'):
                self.screen5 = Screen5()
                self.stackedWidget.addWidget(self.screen5)
                self.stackedWidget.setCurrentWidget(self.screen5)

    def goto_screen(self, screen_index):
        self.stackedWidget.setCurrentIndex(screen_index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
