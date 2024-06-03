# K-Means Clustering Challenge

## Objective:
Implement the K-Means clustering algorithm using Object-Oriented Programming (OOP) principles. The algorithm should be able to handle multiple, large, and complex datasets while maintaining performance.

## Problem Statement:
Implement a class KMeansCluster that performs K-Means clustering on a dataset. The class should have the following functionalities:

1.	Load Data: Load data from a given file.
2.	Initialize Centroids: Randomly initialize the centroids.
3.	Assign Clusters: Assign data points to the nearest centroid.
4.	Update Centroids: Recalculate the centroids based on the assigned clusters.
5.	Iterate: Repeat the assignment and update steps until convergence.
6.	Output Results: Save the clustered data to an output file.

### Class Structure:

*	KMeansCluster
*	__init__(self, input_file: str, k: int, max_iterations: int = 300)
*	load_data(self)
*	initialize_centroids(self)
* assign_clusters(self)
*	update_centroids(self)
*	iterate(self)
*	save_results(self, output_file: str)

### Functional Requirements:

1.	Load Data: The load_data method should read the input file and store the data in an appropriate data structure.
2.	Initialize Centroids: The initialize_centroids method should randomly select k data points as initial centroids.
3.	Assign Clusters: The assign_clusters method should assign each data point to the nearest centroid.
4.	Update Centroids: The update_centroids method should recalculate the centroids as the mean of the assigned data points.
5.	Iterate: The iterate method should repeat the assignment and update steps until the centroids do not change significantly or the maximum number of iterations is reached.
6.	Output Results: The save_results method should write the clustered data and centroids to the specified output file.

### Dataset for Testing

*	Small dataset example:
```json filename=small_dataset.json
  [
    [1.0, 2.0],
    [1.5, 1.8],
    [5.0, 8.0],
    [8.0, 8.0],
    [1.0, 0.6],
    [9.0, 11.0],
    [8.0, 2.0],
    [10.0, 2.0],
    [9.0, 3.0]
  ]
```

* Expected result for this dataset:
```json
{
    "centroids": [
        [9.0, 2.33333333],
        [1.16666667, 1.46666667],
        [7.33333333, 9.0]
    ],
    "labels": [1, 1, 2, 2, 1, 2, 0, 0, 0]
}
```

## Instructions for Students

1.	Implementation:
    * Implement the KMeansCluster class as described in the problem statement.
    * Ensure your code can be executed from the bash command line as `python k-means.py input_file k output_file`.
2.	Testing:
    * Test your implementation with the provided dataset and larger datasets to ensure it meets the performance requirements.
    * Ensure the output matches the expected results.
3.	Submission:
  	* Fork this repository to your github account and submit your code in your repository.
    * Submit your code along with a README file explaining your approach and any assumptions made.
    * Include any test cases you used for validation.
    * Share your repository with me to evaluate your solution.


Good luck!
