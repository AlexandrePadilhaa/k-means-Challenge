import sys
import numpy as np
import json

from kmeans_class import KMeansCluster

#cria um dataset uniformemente distribuido
def create_dataset(filename: str, num_points: int):
    data = np.random.rand(num_points, 2) * 10

    with open(filename, "w") as file:
        json.dump(data.tolist(), file)


def main():
    #Criação de datasets para testes
    create_dataset("dados_100000.json", 100000)

    if len(sys.argv) != 4:
        print("Estrutura: python k-means.py input_file k output_file") #ex: python  k-means.py dados_100000.json 100 output.json
        sys.exit(1)

    input_file = sys.argv[1]
    k = int(sys.argv[2])
    output_file = sys.argv[3]

    print("Arquivo de entrada: ",input_file," K: ",k," Arquivo de saida: ", output_file)

    try:
        kmeans = KMeansCluster(input_file, k)
        kmeans.run(output_file)
        print(f"Resultados salvos em {output_file}")
    except ValueError as e:
        print(f"Erro: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()