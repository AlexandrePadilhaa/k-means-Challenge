# Alexandre Padilha
# Arquivo para explicações sobre abordagem e suposições feitas

# Referencias usadas para estudar o problema 

* Textos
    * https://en.wikipedia.org/wiki/K-means_clustering
    * https://medium.com/cwi-software/entendendo-clusters-e-k-means-56b79352b452
* Videos
    * https://www.youtube.com/watch?v=4b5d3muPQmA&t=375s
    * https://www.youtube.com/watch?v=R2e3Ls9H_fc

* Simulador gráfico
    * https://www.naftaliharris.com/blog/visualizing-k-means-clustering/


# Pseudo codigo Kmeans

    ENTRADA: 
       - Um conjunto de dados D = {(x1, y1), (x2, y2), ..., (xn, yn)}
       - Número de clusters k
       - Critério de parada (ex: número máximo de iterações ou tolerância)

    ESCOLHER k pontos aleatórios como os centróides iniciais {c1, c2, ..., ck}
       - Cada centróide cj é uma coordenada (xj, yj)

    ENQUANTO não convergir ou não atingir o número máximo de iterações:
        PARA cada ponto (xi, yi) em D:
        Calcular a distância de (xi, yi) a cada centróide (xj, yj) usando a distância euclidiana:
            distância = sqrt((xi - xj)^2 + (yi - yj)^2)
            Atribuir o ponto (xi, yi) ao cluster cujo centróide esteja mais próximo

    ATUALIZAR os centróides:
        PARA cada cluster j de 1 até k:
          Calcular o novo centróide (xj, yj) como a média de todos os pontos atribuídos ao cluster j:
              xj = média das coordenadas x dos pontos no cluster j
              yj = média das coordenadas y dos pontos no cluster j

    VERIFICAR convergência:
        Se a mudança nos centróides for menor que a tolerância, então parar

 SAÍDA: Os k clusters e os centróides finais

# Suposições para o problemas
    * As entradas sempre serão pontos bidimencionais
    * A distribuição dos dados é aproximadamente normal. Em caso de outras distribuições existem outras abordagens que podem ser mais eficientes.


# Melhorias possiveis
    
    * Utilizar técnicas como inicialização inteligente de centroides, como o k-means++, que pode melhorar a convergência e a qualidade dos clusters.
    * Paralelizar o algoritmo para processar os cálculos em várias CPUs ou em GPU, para acelerar o tempo de execução especialmente em grandes conjuntos de dados. Para fazer isso, seria necessario o uso de bibliotecas como Dask e SciPy
    * Implementar uma estratégia para lidar com outliers, que podem distorcer os resultados do clustering.

