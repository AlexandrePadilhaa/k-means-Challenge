import sys


from Kmeans_class import KMeansCluster

def main():
    if len(sys.argv) != 4:
        print("Estrutura: python k-means.py input_file k output_file") #ex:  k-means.py small_dataset.json 3 output.json
        sys.exit(1)

    input_file = sys.argv[1]
    k = int(sys.argv[2])
    output_file = sys.argv[3]

    print("Arquivo de entrada: ",input_file," K: ",k," Arquivo de saida: ", output_file)

    k_means_object = KMeansCluster(input_file,k)


    k_means_object.load_data()
    print("data:", k_means_object.data)


    k_means_object.initialize_centroids()
    print("centroids:", k_means_object.centroids)

 
    k_means_object.assign_clusters()
    print("labels:", k_means_object.labels)

    
    new_centroids = k_means_object.update_centroids()
    print("atualizados centroids:", new_centroids)

    k_means_object.iterate()
    print("centroids finais:", k_means_object.centroids)

    k_means_object.save_results(output_file)
    print("Resultado salvos em:", output_file)


if __name__ == "__main__":
    main()