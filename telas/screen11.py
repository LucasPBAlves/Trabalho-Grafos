from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, \
    QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal
from collections import defaultdict

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

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def testIfGraphIsBipartite(self):
        # Parse the edges from SharedState
        arestas_str = SharedState.get_aresta().split(';')
        graph = defaultdict(list)
        for aresta in arestas_str:
            v1, v2 = aresta.split('-')
            graph[v1].append(v2)
            graph[v2].append(v1)  # Assuming the graph is undirected

        # Initialize color for each vertex
        color = {vertex: -1 for vertex in graph}

        # Function to check bipartite using DFS
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
            QMessageBox.information(self, "Resultado", "O grafo é bipartido.")
        else:
            QMessageBox.information(self, "Resultado", "O grafo não é bipartido.")


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen11()
    screen.show()
    sys.exit(app.exec())
