from collections import defaultdict
import heapq
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QMessageBox

from shared_state import SharedState

class Screen19(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Caminho Mínimo (Dijkstra)")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        # Adicionando o espaçamento no topo para centralizar verticalmente
        layout.addItem(QSpacerItem(20, 60, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        instructionLabel = QLabel("Insira os vértices de origem e destino para encontrar o caminho mínimo:", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)

        # Caixa de entrada do vértice de origem
        self.originInput = QLineEdit(self)
        self.originInput.setPlaceholderText("Vértice de origem")
        self.originInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.originInput.setMinimumWidth(150)
        self.originInput.setFixedHeight(40)
        layout.addWidget(self.originInput, alignment=Qt.AlignmentFlag.AlignCenter)

        # Caixa de entrada do vértice de destino
        self.destinationInput = QLineEdit(self)
        self.destinationInput.setPlaceholderText("Vértice de destino")
        self.destinationInput.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.destinationInput.setMinimumWidth(150)
        self.destinationInput.setFixedHeight(40)
        layout.addWidget(self.destinationInput, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botão para testar o algoritmo
        testButton = QPushButton("Testar", self)
        testButton.clicked.connect(self.findShortestPath)
        layout.addWidget(testButton, alignment=Qt.AlignmentFlag.AlignCenter)

        # Label para exibir o resultado
        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)

        # Adiciona um espaçador extra para empurrar o botão "Voltar" para baixo
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Botão para voltar, na parte inferior
        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignRight)

        self.setLayout(layout)

    def findShortestPath(self):
        origin = self.originInput.text().strip()
        destination = self.destinationInput.text().strip()

        if not origin or not destination:
            QMessageBox.warning(self, "Entrada Inválida", "Por favor, insira ambos os vértices de origem e destino.")
            return

        edges_str = SharedState.get_aresta()
        is_directed = SharedState.get_is_directed()
        if not edges_str:
            QMessageBox.warning(self, "Erro", "Não há arestas definidas no grafo.")
            return

        graph = defaultdict(list)
        vertices = set()

        for edge in edges_str.split(';'):
            try:
                v1, v2, weight = edge.split('-')
                weight = int(weight)
                graph[v1].append((v2, weight))
                vertices.update([v1, v2])
                if not is_directed:
                    graph[v2].append((v1, weight))
            except ValueError:
                QMessageBox.warning(self, "Erro de Formato", f"A aresta '{edge}' não está no formato correto.")
                return

        if origin not in vertices or destination not in vertices:
            QMessageBox.warning(self, "Erro", "Os vértices de origem ou destino não existem no grafo.")
            return

        distances = {v: float('inf') for v in vertices}
        distances[origin] = 0
        prev = {v: None for v in vertices}

        heap = []
        heapq.heappush(heap, (0, origin))

        while heap:
            current_dist, current_vertex = heapq.heappop(heap)

            if current_dist > distances[current_vertex]:
                continue

            for neighbor, weight in graph[current_vertex]:
                distance = current_dist + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    prev[neighbor] = current_vertex
                    heapq.heappush(heap, (distance, neighbor))

        if distances[destination] == float('inf'):
            self.resultLabel.setText(f"Não foi possível encontrar um caminho entre {origin} e {destination}.")
        else:
            path = []
            current = destination
            while current:
                path.append(current)
                current = prev[current]
            path.reverse()
            self.resultLabel.setText(f"Caminho mínimo de {origin} a {destination} é: {' -> '.join(path)} (distância: {distances[destination]})")
