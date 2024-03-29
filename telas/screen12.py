from tkinter import messagebox
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal
from shared_state import SharedState

class Screen12(QDialog):
    backSignal = pyqtSignal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Mostrar Matriz de Adjacência")
        self.setGeometry(100, 100, 600, 400)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        instructionLabel = QLabel("Clique no botão abaixo para mostrar a Lista de adjacência do grafo.", self)
        instructionLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructionLabel)
         # Layout horizontal para centralizar o botão
        buttonLayout = QHBoxLayout()
        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))

        testButton = QPushButton("Mostrar Lista de Adjacência", self)
        testButton.clicked.connect(self.showMatrix)
        buttonLayout.addWidget(testButton)

        buttonLayout.addItem(QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(buttonLayout)

         # Label para exibir a matriz de adjacência
        self.resultLabel = QLabel("", self)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.resultLabel)
        # Padding no fundo
        layout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        

        backButton = QPushButton("Voltar", self)
        backButton.clicked.connect(self.backSignal.emit)
        layout.addWidget(backButton, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def  showMatrix(self):
            arestas_str = SharedState.get_aresta()
            if not arestas_str:
                print('Erro')
                return
            isDirected = SharedState.get_is_directed()

            arestas = arestas_str.split(';')
            vertices = []

            for aresta in arestas:
                v1, v2 = aresta.split('-')
                if v1 not in vertices:
                    vertices.append(v1)
                if v2 not in vertices:
                    vertices.append(v2)

                num_vertices = len(vertices)

                adjacencyMatrix = [[0] * num_vertices for _ in range (num_vertices)]
                vertex_to_index = {vertex: index for index, vertex in enumerate(vertices)}

                for aresta in arestas:
                    v1,v2 = aresta.split('-')
                    idx1  = vertex_to_index.get(v1)
                    idx2 = vertex_to_index.get(v2)

                    if v1 not in vertex_to_index or v2 not in vertex_to_index:
                        print(f"Erro: Um ou ambos os vértices da aresta {aresta} não estão presentes no dicionário de índices.")
                        continue

                    adjacencyMatrix[idx1][idx2] = 1
                    if not isDirected:
                        adjacencyMatrix[idx2][idx1] = 1

                    matriz_str = ""

                    for row in adjacencyMatrix:
                        matriz_str += "\t".join(map(str, row)) + "\n"
                        
                        self.resultLabel.setText(matriz_str)
                        
                    
                        
                    

               

            

            
            

    


   
                
              
               
            
                    
        

             
           
                


            

          
        
       

        

       
           

           

            

           
           


           
                


          
            
            
          

    
                     
         
    

if __name__ == '__main__':
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    screen = Screen12()
    screen.show()
    sys.exit(app.exec())
