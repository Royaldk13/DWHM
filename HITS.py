import numpy as np

def hits_algorithm(matrix, num_iterations=100):
    n = len(matrix)  # Number of pages/nodes

    # Initialize hub and authority scores to 1
    hubs = np.ones(n)
    authorities = np.ones(n)

    # Iteratively calculate hub and authority scores
    for iteration in range(1, num_iterations + 1):
        # Update authority scores: a = A^T * h
        authorities = np.dot(matrix.T, hubs)
        
        # Update hub scores: h = A * a
        hubs = np.dot(matrix, authorities)
        
        # Normalize the hub and authority scores to prevent overflow
        authorities = authorities / np.linalg.norm(authorities, ord=2)
        hubs = hubs / np.linalg.norm(hubs, ord=2)

        # Print the hub and authority scores for each iteration
        print(f"Iteration {iteration}:")
        print("Authorities:", authorities)
        print("Hubs:", hubs)
        print("")

    return hubs, authorities

def main():
    # Take user input for the number of pages
    n = int(input("Enter the number of pages: "))
    
    # Initialize the adjacency matrix
    print(f"Enter the adjacency matrix (enter 1 if there is a link, 0 otherwise):")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    # Convert the matrix to a numpy array
    matrix = np.array(matrix)

    # Number of iterations for convergence
    num_iterations = int(input("Enter the number of iterations: "))

    # Call the HITS algorithm and print the final hub and authority scores
    hubs, authorities = hits_algorithm(matrix, num_iterations)

    print("\nFinal Hub Scores:", hubs)
    print("Final Authority Scores:", authorities)

if __name__ == '__main__':
    main()
