# main.py - Atualizado para PyQt6
import sys
from PyQt6.QtWidgets import QApplication
from mainwindow import MainWindow

def main():
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
