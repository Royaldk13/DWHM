import numpy as np

def page_rank(matrix, num_iterations=100, damping_factor=0.85):
    # Number of pages
    n = len(matrix)
    
    # Initialize the rank vector with equal probability for all pages
    ranks = np.ones(n) / n
    
    # Transition matrix
    matrix = np.array(matrix, dtype=float)
    
    # Normalize matrix (make columns sum to 1 to represent probabilities)
    for i in range(n):
        if np.sum(matrix[:, i]) != 0:
            matrix[:, i] /= np.sum(matrix[:, i])
        else:
            matrix[:, i] = np.ones(n) / n  # Handle dangling nodes (no out-links)

    # PageRank iterative calculation
    for iteration in range(1, num_iterations + 1):
        # Apply the PageRank formula
        new_ranks = (1 - damping_factor) / n + damping_factor * np.dot(matrix, ranks)
        
        # Print ranks for each iteration
        print(f"Iteration {iteration}: {new_ranks}")
        
        # Check for convergence (if the difference between iterations is very small)
        if np.allclose(ranks, new_ranks, atol=1e-6):
            print(f"Converged after {iteration} iterations.")
            break
        
        # Update the rank values
        ranks = new_ranks
    
    return ranks

def main():
    # Take user input for the number of pages
    n = int(input("Enter the number of pages: "))
    
    # Initialize the adjacency matrix
    print(f"Enter the adjacency matrix (enter 1 if there is a link, 0 otherwise):")
    matrix = []
    for i in range(n):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)
    
    # Number of iterations and damping factor
    num_iterations = int(input("Enter the number of iterations: "))
    damping_factor = float(input("Enter the damping factor (usually 0.85): "))

    # Call the PageRank function and print the final ranks
    final_ranks = page_rank(matrix, num_iterations, damping_factor)
    print("\nFinal Page Ranks:", final_ranks)

if __name__ == '__main__':
    main()
