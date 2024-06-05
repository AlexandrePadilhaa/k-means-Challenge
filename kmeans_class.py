import numpy as np
import json
import sys

class KMeansCluster:

    #Método construtor da classe
    def __init__(self, input_file: str, k: int, max_iterations: int = 300):
        #atributos da classe
        self.input_file = input_file
        self.k = k
        self.max_iterations = max_iterations
        self.data = None
        self.centroids = None
        self.labels = None
    
    #carrega entrada a partir do arquivo de input
    def load_data(self):
        try:
            with open(self.input_file, 'r') as file:
                self.data = np.array(json.load(file))
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.input_file}' não foi encontrado.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Erro: O arquivo '{self.input_file}' não está no formato JSON válido.")
            sys.exit(1)

    #Inicialização centroides (aleatoriamente)
    def initialize_centroids(self):
        np.random.seed(42)
        indices = np.random.choice(len(self.data), self.k, replace=False)
        self.centroids = self.data[indices]
    
    def assign_clusters(self):
        distances = np.linalg.norm(self.data[:, np.newaxis] - self.centroids, axis=2)
        self.labels = np.argmin(distances, axis=1)
    
    def update_centroids(self):
        new_centroids = np.array([self.data[self.labels == i].mean(axis=0) for i in range(self.k)])
        return new_centroids
    
    def iterate(self):
        for _ in range(self.max_iterations):
            old_centroids = np.copy(self.centroids)
            self.assign_clusters()
            self.centroids = self.update_centroids()
            if np.allclose(old_centroids, self.centroids):
                break
    
    def save_results(self, output_file: str):
        results = {
            "centroids": self.centroids.tolist(),
            "labels": self.labels.tolist()
        }
        with open(output_file, 'w') as file:
            json.dump(results, file)