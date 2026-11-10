def adjacency_list_to_matrix(adj_list):
    n = len(adj_list)
    adj_matrix = [[0] * n for _ in range(n)]

    # #Convert the adjacency list to an adjacency matrix
    for row, val in adj_list.items():
        for e in val:
            adj_matrix[row][e] = 1      

    # Print each row in the adjacency matrix.
    for row in adj_matrix:
        print(row)

    # Return the adjacency matrix.
    return adj_matrix

adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})