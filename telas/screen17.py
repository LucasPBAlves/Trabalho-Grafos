from collections import defaultdict

from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, QMessageBox

from shared_state import SharedState

class Screen17(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("AGM Usando o Kruskal")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        instructionLabel = QLabel("Clique no botão abaixo para mostrar o resultado de Kruskal.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        testButton = QPushButton("Testar", self)
        testButton.clicked.connect(self.AGM_Kruskal)
        layout.addWidget(testButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def AGM_Kruskal(self):
        arestas_str = SharedState.get_aresta()
        if not arestas_str:
            QMessageBox.warning(self, "Aviso", "Não há arestas definidas no grafo.")
            return

        # Parse arestas e peso
        edges = []
        for aresta in arestas_str.split(';'):
            try:
                v1, v2, peso = aresta.split('-')
                edges.append((int(peso), v1, v2))  # armazena como (peso, v1, v2)
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{aresta}' não está no formato correto.")
                return

        # Ordena as arestas por peso
        edges.sort()

        # Estrutura para encontrar e unir conjuntos
        pai = {}
        nivel = {}

        def find(v):
            if pai[v] != v:
                pai[v] = find(pai[v])
            return pai[v]

        def uniao(v1, v2):
            raiz1 = find(v1)
            raiz2 = find(v2)
            if raiz1 != raiz2:
                if nivel[raiz1] > nivel[raiz2]:
                    pai[raiz2] = raiz1
                else:
                    pai[raiz1] = raiz2
                    if nivel[raiz1] == nivel[raiz2]:
                        nivel[raiz2] += 1

        # Inicializa os conjuntos disjuntos
        for _, v1, v2 in edges:
            pai[v1] = v1
            pai[v2] = v2
            nivel[v1] = 0
            nivel[v2] = 0

        # Algoritmo de Kruskal
        mst = []
        for peso, v1, v2 in edges:
            if find(v1) != find(v2):
                uniao(v1, v2)
                mst.append((v1, v2, peso))

        # Formata a saída da AGM
        if mst:
            result = "Arestas da Árvore Geradora Mínima:\n" + "\n".join([f"{v1} - {v2} (peso: {peso})" 
                                                                         
        for v1, v2, peso in mst])
        else:
            result = "Não foi possível gerar uma árvore mínima."

        # Exibe o resultado na etiqueta
        self.resultLabel.setText(result)