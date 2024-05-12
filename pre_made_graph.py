from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QMessageBox
from PyQt6.QtCore import pyqtSignal
from shared_state import SharedState

class PreMadeGraphScreen(QWidget):
    backSignal = pyqtSignal()
    nextSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Pre-Made Graph")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout(self)

        instructionLabel = QLabel("Select a pre-made graph from the options below:", self)
        layout.addWidget(instructionLabel)

        graphs = [
            ("Dir - A - Z",
             "A-B-2;B-C-3;C-D-1;D-E-2;E-F-3;F-G-1;G-H-2;H-I-3;I-J-4;J-K-1;K-L-2;L-M-3;M-N-4;N-O-1;O-P-2;P-Q-3;Q-R-4;R-S-1;S-T-2;T-U-3;U-V-4;V-W-1;W-X-2;X-Y-3;Y-Z-4",True),
            ("NotDir - A - Z","A-B-5;B-C-4;C-D-3;D-E-5;E-F-2;F-G-1;G-H-3;H-I-5;I-J-1;J-K-2;K-L-3;L-M-4;M-N-1;N-O-5;O-P-3;P-Q-1;Q-R-2;R-S-4;S-T-3;T-U-1;U-V-5;V-W-2;W-X-4;X-Y-1;Y-Z-2",False),
            ("Dir - A - M", "A-B-1;B-C-2;C-D-1;D-E-3;E-F-4;F-G-5;G-H-4;H-I-3;I-J-2;J-K-1;K-L-2;L-M-3;M-A-4", True),
            ("NotDir - A - O","A-B-1;B-C-2;C-D-3;D-E-1;E-F-2;F-G-3;G-H-1;H-I-2;I-J-3;J-K-1;K-L-2;L-M-3;M-N-1;N-O-2;O-A-3", False),
            ("Dir - P - Z", "P-Q-1;Q-R-2;R-S-3;S-T-4;T-U-1;U-V-2;V-W-3;W-X-4;X-Y-1;Y-Z-2;Z-P-3", True),
            ("NotDir - A - E", "A-B-3;B-C-2;C-D-5;D-E-4;E-A-1", False),
            ("Dir - F - J", "F-G-2;G-H-3;H-I-1;I-J-4;J-F-2", True),
            ("NotDir - K - O", "K-L-1;L-M-3;M-N-4;N-O-2;O-K-5", False),
            ("Dir - P - T", "P-Q-2;Q-R-3;R-S-1;S-T-4;T-P-5", True),
            ("NotDir - U - Z", "U-V-2;V-W-3;W-X-1;X-Y-4;Y-Z-2;Z-U-3", False)
        ]

        for label, edges, is_directed in graphs:
            btn = QPushButton(label, self)
            btn.clicked.connect(lambda ch, e=edges, d=is_directed: self.selectGraph(e, d))
            layout.addWidget(btn)

        backButton = QPushButton("Back", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton)

        self.setLayout(layout)

    def selectGraph(self, edges, is_directed):
        SharedState.set_aresta(edges)
        SharedState.set_is_directed(is_directed)
        QMessageBox.information(self, "Graph Selected", f"Graph {'directed' if is_directed else 'non-directed'} - Edges: {edges}")
        self.nextSignal.emit()

if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = PreMadeGraphScreen()
    screen.show()
    sys.exit(app.exec())
