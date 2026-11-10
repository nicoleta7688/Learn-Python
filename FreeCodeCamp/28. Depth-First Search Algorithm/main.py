def dfs(adj_matrix, node_label):
    stack = []
    visited = []

    # 1. Add the starting node to the stack.
    stack.append(node_label)

    # 2. Continue while the stack is not empty.
    while stack:

        # 3. Pop the last node from the stack.
        current_node = stack.pop()

        # 4. Skip the node if it was already visited.
        if current_node in visited:
            continue

        # 5. Mark the current node as visited.
        visited.append(current_node)

        # 6. Find all unvisited neighbors.
        childs = []

        for index, edge in enumerate(adj_matrix[current_node]):
            if edge == 1:
                if index not in visited and index not in stack:
                    childs.append(index)

        # 7. Add neighbors in reverse order (ascending traversal).
        childs.reverse()
        stack.extend(childs)

    return visited


print(dfs(
    [[0, 1, 0, 0],
     [1, 0, 1, 0],
     [0, 1, 0, 1],
     [0, 0, 1, 0]],
    1
))