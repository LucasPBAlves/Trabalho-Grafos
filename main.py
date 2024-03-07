# main.py - Atualizado para PyQt6
import sys
from PyQt6.QtWidgets import QApplication
from mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
