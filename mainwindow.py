import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QIcon
from styles import DARK_THEME_STYLE
import warnings
# Importe suas telas aqui
from screen1 import Screen1

warnings.filterwarnings("ignore", category=DeprecationWarning)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.currentScreenIndex = {}  # Para gerenciar os índices das telas
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Grafos')
        self.setGeometry(350, 100, 1280, 720)
        self.setStyleSheet(DARK_THEME_STYLE)
        self.setWindowIcon(QIcon('assets/graph.ico'))

        self.stackedWidget = QStackedWidget()
        self.setCentralWidget(self.stackedWidget)

        self.setupInitialScreen()
        self.setupScreen1()  # Preparar a Screen1 e adicionar ao QStackedWidget

    def setupInitialScreen(self):
        initialWidget = QWidget()
        layout = QVBoxLayout(initialWidget)

        title = QLabel('Implementação de Grafos', initialWidget)
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet("font-size: 24pt; font-weight: bold; font-family: Arial;")
        layout.addWidget(title)

        layout.addItem(QSpacerItem(15, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        manip_subtitle = QLabel('Escolha uma opção:', initialWidget)
        manip_subtitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(manip_subtitle)

        # Botões centralizados
        buttons_layout = QVBoxLayout()
        createGraphButton = QPushButton("Criação de um grafo com X vértices", initialWidget)
        createGraphButton.clicked.connect(lambda: self.gotoScreen('Screen1'))
        createGraphButton.setMinimumHeight(40)
        createGraphButton.setMaximumWidth(400)
        buttons_layout.addWidget(createGraphButton)

        usePredefinedGraphButton = QPushButton("Usar grafos já plotados", initialWidget)
        usePredefinedGraphButton.clicked.connect(self.notImplementedYet)
        usePredefinedGraphButton.setMinimumHeight(40)
        usePredefinedGraphButton.setMaximumWidth(400)
        buttons_layout.addWidget(usePredefinedGraphButton)

        h_layout = QHBoxLayout()
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        h_layout.addLayout(buttons_layout)
        h_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(h_layout)

        self.stackedWidget.addWidget(initialWidget)
        self.currentScreenIndex['InitialScreen'] = 0  # Índice da tela inicial

    def setupScreen1(self):
        # Supondo que Screen1 esteja corretamente definida para funcionar com QStackedWidget
        self.screen1 = Screen1()
        self.stackedWidget.addWidget(self.screen1)
        self.currentScreenIndex['Screen1'] = self.stackedWidget.count() - 1

    def returnToInitialScreen(self):
        self.stackedWidget.setCurrentIndex(0)
    def gotoScreen(self, screenName):
        if screenName in self.currentScreenIndex:
            self.stackedWidget.setCurrentIndex(self.currentScreenIndex[screenName])

    def returnToInitialScreen(self):
        self.stackedWidget.setCurrentIndex(self.currentScreenIndex['InitialScreen'])
    def notImplementedYet(self):
        print("Função não implementada")

if __name__ == '__main__':
    app = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec())
