from collections import defaultdict

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, \
    QSpacerItem, QSizePolicy, QMessageBox

from shared_state import SharedState


class Screen16(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Ordenação Topológica")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        label = QLabel("Clique para mostrar a Ordenação Topológica:", self)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)

        layout.addItem(QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))

        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        testButton = QPushButton("Ordenação Topológica", self)
        testButton.setFixedSize(200, 40)
        testButton.clicked.connect(self.Ordenacao_topologica)
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

    def Ordenacao_topologica(self):
        arestas_str = SharedState.get_aresta()
        if not arestas_str:
            QMessageBox.warning(self, "Erro", "Não há arestas definidas.")
            return

        arestas = arestas_str.split(';')
        adjacencia = defaultdict(list)
        grau_entrada = defaultdict(int)

        # Construir lista de adjacência e calcular o grau de entrada de cada vértice
        for aresta in arestas:
            try:
                v1, v2, _ = aresta.split('-')  # Peso não é utilizado para ordenação topológica
                adjacencia[v1].append(v2)
                grau_entrada[v2] += 1
                if v1 not in grau_entrada:
                    grau_entrada[v1] = 0  # Inicializar grau de entrada como 0 para vértices que não recebem arestas
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{aresta}' não está no formato correto.")

        # Lista para armazenar a ordenação topológica
        ordenacao_topologica = []

        # Lista para armazenar vértices com grau de entrada zero
        lista = [v for v in grau_entrada if grau_entrada[v] == 0]

        # Executar o algoritmo de Kahn
        while lista:
            vertice = lista.pop(0)
            ordenacao_topologica.append(vertice)
            for vizinho in adjacencia[vertice]:
                grau_entrada[vizinho] -= 1
                if grau_entrada[vizinho] == 0:
                    lista.append(vizinho)

        # Verificar se a ordenação topológica foi bem-sucedida
        if len(ordenacao_topologica) == len(grau_entrada):
            ordenacao_topologica_str = ' -> '.join(ordenacao_topologica)
            self.resultLabel.setText(f"Ordenação topológica: {ordenacao_topologica_str}.")
        else:
            self.resultLabel.setText("O grafo contém um ciclo e não pode ser ordenado topologicamente.")


if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen16()
    screen.show()
    sys.exit(app.exec())
