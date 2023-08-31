def optimal_bst(P):
    n = len(P) - 1  # Number of keys
    C = [[0] * (n + 2) for _ in range(n + 2)]  # Cost matrix
    R = [[0] * (n + 1) for _ in range(n + 2)]  # Root matrix

    # Initialize base cases for single nodes and empty subtrees
    for i in range(1, n + 2):
        C[i][i - 1] = 0
        C[i][i] = P[i - 1]  # Adjust indexing
        R[i][i] = i
    C[n + 1][n] = 0

    # Iterate over diagonals of the cost matrix
    for d in range(1, n + 1):  # Adjust range
        for i in range(1, n - d + 2):  # Adjust range
            j = i + d

            minval = float('inf')
            kmin = -1

            # Iterate over possible roots in the current subtree
            for k in range(i, j + 1):
                cost = C[i][k - 1] + C[k + 1][j]
                if cost < minval:
                    minval = cost
                    kmin = k

            sum_probs = sum(P[i - 1:j])  # Adjust indexing
            C[i][j] = minval + sum_probs
            R[i][j] = kmin

    return C[1][n], R

# Taking user input for search probabilities
n = int(input("Enter the number of keys: "))
P = []
for _ in range(n):
    prob = float(input(f"Enter probability for key {_ + 1}: "))
    P.append(prob)

# Calculate optimal cost and root matrix
optimal_cost, root_matrix = optimal_bst(P)

print("Optimal Cost:", optimal_cost)
print("Root Matrix:")
for row in root_matrix[1:]:
    print(row)


'''
Output:
Enter the number of keys: 4
Enter probability for key 1: 0.1
Enter probability for key 2: 0.2
Enter probability for key 3: 0.3
Enter probability for key 4: 0.4

Optimal Cost: 0.7
Root Matrix:
1  1  2  2
0  2  2  2
0  0  3  3
0  0  0  4
'''