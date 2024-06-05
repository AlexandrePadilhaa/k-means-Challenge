import numpy as np
import json
import sys

class KMeansCluster:

    #Método construtor da classe
    def __init__(self, input_file: str, k: int, max_iterations: int = 300):

        if k <= 0:
            raise ValueError("O valor de k deve ser maior que 0.")
        if max_iterations <= 0:
            raise ValueError("O número máximo de iterações deve ser maior que 0.")
    
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
            if self.k <= 0 or self.k > len(self.data):
                raise ValueError("O valor de k deve ser maior que 0 e menor ou igual ao número de pontos de dados.")
        except FileNotFoundError:
            print(f"Erro: O arquivo '{self.input_file}' não foi encontrado.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"Erro: O arquivo '{self.input_file}' não está no formato JSON válido.")
            sys.exit(1)
        except ValueError as e:
            print(e)
            sys.exit(1)

    #Inicialização centroides (aleatoriamente)
    def initialize_centroids(self):
        np.random.seed(42) # Semente do gerador de números aleatórios
        indices = np.random.choice(len(self.data), self.k, replace=False)
        self.centroids = self.data[indices]
    
    def assign_clusters(self):
        # Calcula as distâncias de cada ponto de dados aos centróides usando a distancia euclidiana
        distances = np.linalg.norm(self.data[:, np.newaxis] - self.centroids, axis=2)
        # Atribui cada ponto ao cluster mais proximo
        self.labels = np.argmin(distances, axis=1)
    
    def update_centroids(self):
        # Calcula os novos centróides como a média dos pontos em cada cluster
        new_centroids = np.array([self.data[self.labels == i].mean(axis=0) for i in range(self.k)])
        return new_centroids
    
    def iterate(self):
        # Itera até atingir o número máximo de iterações ou ocorrer a convergência antecipada
        for _ in range(self.max_iterations):
            old_centroids = np.copy(self.centroids) # salva centroides anteriores
            self.assign_clusters() # atribui cada ponto ao cluster mais proximo
            self.centroids = self.update_centroids() # recalcula os centroides
            if np.allclose(old_centroids, self.centroids): # verifica se o algoritimo atingiu a convergencia antecipada, quando os centroides não mudam singificativamente
                break
    
    def save_results(self, output_file: str):
        results = {
            "centroids": self.centroids.tolist(),
            "labels": self.labels.tolist()
        }
        with open(output_file, 'w') as file:
            json.dump(results, file)

    def run(self, output_file: str):
       
        self.load_data()
        self.initialize_centroids()
        self.iterate()
        self.save_results(output_file)