# Implement K-means clustering with 2 clusters
print("Enter the number of values")
n = 13

values = [13, 16, 29, 78, 21, 43, 56, 90, 21, 8, 88, 60, 34]
values = [[value, 0] for value in values]

# Initialize centroids (First two values from the dataset)
c1 = values[0][0]
c2 = values[1][0]

for _ in range(10):  # Iterate multiple times to refine the clusters
    count1 = count2 = total1 = total2 = 0

    # Assign values to clusters based on proximity to centroids
    for i in range(len(values)):
        if abs(values[i][0] - c1) <= abs(values[i][0] - c2):
            count1 += 1
            total1 += values[i][0]
            values[i][1] = 1  # Assign to cluster 1
        else:
            count2 += 1
            total2 += values[i][0]
            values[i][1] = 2  # Assign to cluster 2

    # Recompute centroids for both clusters
    c1 = float(total1 / count1) if count1 != 0 else 0
    c2 = float(total2 / count2) if count2 != 0 else 0

# Output the final clusters
print("\nFinal Clustering Result:")
for value in values:
    print(f"Value: {value[0]}, Cluster: {value[1]}")

print(f"\nFinal Centroid 1: {c1}")
print(f"Final Centroid 2: {c2}")
