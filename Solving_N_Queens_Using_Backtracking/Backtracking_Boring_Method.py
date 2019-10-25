
import copy
def create_chess_board(size_of_board):
    board = [0] * int(size_of_board)
    for i in range(int(size_of_board)):
        board[i] = [0] * int(size_of_board)
    #print(board)
    return board


def can_we_place_a_queen_here(board, row, col, size_of_board):

    '''Check if any spot to the left of this position has a Queen'''
    for item in range(col):
        if board[row][item] == 1:
            return False
    i = row - 1
    j = col - 1

    '''check upper left diagonal'''
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    i_new = row + 1
    j_new = col - 1

    '''check lower left diagonal'''
    while i_new < size_of_board and j_new >= 0:
        if board[i_new][j_new] == 1:
            return False
        i_new += 1
        j_new -= 1

    return True

def append_this_solution(board):
    global solutions
    all_solutions_list.append(copy.deepcopy(board))


def n_queens_solver(board, col, size_of_board):

    if col >= size_of_board:
        return True

    for i in range(size_of_board):

        if can_we_place_a_queen_here(board, i, col, size_of_board):

            board[i][col] = 1
            if col == size_of_board - 1:

                append_this_solution(board)
                board[i][col] = 0
                return True
            '''If not true, we do this.'''
            n_queens_solver(board, col + 1, size_of_board)
            board[i][col] = 0





if __name__ == "__main__":
    from itertools import compress, count
    import numpy as np

    size_of_board = int(input("What is the size of the board?"))
    chess_board = create_chess_board(size_of_board)
    all_solutions_list = []
    n_queens_solver(chess_board, 0, size_of_board)

    final_solutions_list = []
    for solution in all_solutions_list:
        import time
        solu = []
        print(solution)
        for row in solution:
            solu.append(np.argmax(row))
        final_solutions_list.append(solu)
    print(final_solutions_list)







