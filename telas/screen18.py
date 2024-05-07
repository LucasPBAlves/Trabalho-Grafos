from collections import defaultdict

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, \
    QSizePolicy, QMessageBox

from shared_state import SharedState


class Screen18(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Testar se o Grafo é Conexo")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        label = QLabel("Clique para testar se o grafo é conexo:", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        testButton = QPushButton("Testar Conectividade", self)
        testButton.setFixedSize(200, 40)
        testButton.clicked.connect(self.testConexo)
        buttonLayout.addWidget(testButton)

        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        layout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        backButton = QPushButton("Voltar", self)
        backButton.setFixedSize(200, 40)
        backButtonLayout = QHBoxLayout()
        backButtonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        backButtonLayout.addWidget(backButton)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addLayout(backButtonLayout)

        self.setLayout(layout)

    def testConexo(self):
        arestas_str = SharedState.get_aresta()
        if not arestas_str:
            QMessageBox.warning(self, "Erro", "Não há arestas definidas.")
            return

        direto = SharedState.get_is_directed()
        adjacencia = defaultdict(list)

        # Construir lista de adjacência
        for aresta in arestas_str.split(';'):
            try:
                v1, v2, _ = aresta.split('-')  # Peso ignorado, pois não é relevante aqui
                adjacencia[v1].append(v2)
                if not direto:
                    adjacencia[v2].append(v1)
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{aresta}' não está no formato correto.")

        if not adjacencia:
            self.resultLabel.setText("O grafo não possui vértices ou arestas.")
            return

        visitados = set()

        # Função para fazer busca em profundidade
        def dfs(vertice):
            visitados.add(vertice)
            for vizinho in adjacencia[vertice]:
                if vizinho not in visitados:
                    dfs(vizinho)

        # Executar busca em profundidade a partir de um vértice
        vertice_inicial = next(iter(adjacencia.keys()))
        dfs(vertice_inicial)

        # Verificar se todos os vértices foram visitados
        if len(visitados) == len(adjacencia):
            self.resultLabel.setText("O grafo é conexo.")
        else:
            self.resultLabel.setText("O grafo não é conexo.")


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen18()
    screen.show()
    sys.exit(app.exec())
