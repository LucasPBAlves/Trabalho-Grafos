from collections import defaultdict

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy

from shared_state import SharedState


class Screen11(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o grafo é bipartido")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        instructionLabel = QLabel("Clique no botão abaixo para testar se o grafo é bipartido.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        testButton = QPushButton("Testar", self)
        testButton.clicked.connect(self.testIfGraphIsBipartite)
        buttonLayout.addWidget(testButton)

        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def testIfGraphIsBipartite(self):
        arestas_str = SharedState.get_aresta().split(';')
        graph = defaultdict(list)
        for aresta in arestas_str:
            v1, v2 = aresta.split('-')
            graph[v1].append(v2)
            graph[v2].append(v1)

        color = {vertex: -1 for vertex in graph}

        def isBipartiteDFS(pos, c):
            if color[pos] != -1 and color[pos] != c:
                return False
            color[pos] = c
            ans = True
            for i in graph[pos]:
                if color[i] == -1:
                    ans &= isBipartiteDFS(i, 1 - c)
                if color[i] == c:
                    return False
            return ans

        bipartite = True
        for vertex in graph:
            if color[vertex] == -1:
                bipartite &= isBipartiteDFS(vertex, 0)

        if bipartite:
            self.resultLabel.setText("O grafo é bipartido.")
        else:
            self.resultLabel.setText("O grafo não é bipartido.")


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen11()
    screen.show()
    sys.exit(app.exec())
