def dfs_n_queens(n):
    if n < 1:
        return []

    solutions = []
    board = []

    def backtrack(row):
        if row == n:
            solutions.append(board.copy())
            return

        for column in range(n):
            good_choice = True
            for queen_row, queen_column in enumerate(board):
                if column == queen_column or abs(row - queen_row) == abs(column - queen_column):
                    # nu punem regina daca sunt regine pe aceiasi coloana sau pe aceeasi diagonala
                    good_choice = False
                    break
        
            if good_choice:
                board.append(column)
                backtrack(row + 1)
                board.pop()

    backtrack(0)

    return solutions

print(dfs_n_queens(5))