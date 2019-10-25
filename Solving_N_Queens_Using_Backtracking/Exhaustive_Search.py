'''Methods for n-Queens problem. This file contains methods for both exhaustive serach as we as backtracking.'''

def create_chess_board(size_of_board):
    board = [0] * (size_of_board)
    for i in range(size_of_board):
        board[i] = [0] * size_of_board
    #print(board)
    return board


def check(board, permu, size_of_board):
    print(board,permu)


    '''Check Sideways, to the left and to the right.'''
    for item in range(len(permu)):
        if board[permu[item]][item] == 1 and item != permu[item]:
            return False

    '''Check Upper Left'''
    for item in range(len(permu)):

        item_row = item-1

        item_col = permu[item]-1

        while item_row >= 0 and item_col >= 0:
            if board[item_row][item_col] == 1:
                return False
            item_row -= 1
            item_col -= 1

        '''Check Upper Right'''
        item_row = item - 1

        item_col = permu[item] + 1

        while item_row >= 0 and item_col < size_of_board:
            if board[item_row][item_col] == 1:
                return False
            item_row -= 1
            item_col += 1
        '''Check Lower Left'''
        item_row = item + 1

        item_col = permu[item] - 1

        while item_row < size_of_board and item_col >= 0:
            print(item_row,item_col)
            if board[item_row][item_col] == 1:
                return False
            item_row += 1
            item_col -= 1

        '''Lower Right'''
        item_row = item + 1

        item_col = permu[item] + 1

        while item_row < size_of_board and item_col < size_of_board:
            if board[item_row][item_col] == 1:
                return False
            item_row += 1
            item_col += 1


    return True




def E_Queens(size):
    import time
    start_time = time.time()
    # size_of_board = int(input("Enter the size of n such that the size of the chess board is n * n."))
    # print("The size of the board is: ", size_of_board)
    size_of_board = size
    solutionss = []

    '''Create the board'''
    chess_board = create_chess_board(size_of_board)

    '''Exhaustively search for every combination of the board'''
    from itertools import permutations

    input = [i for i in range(size_of_board)]

    l = list(permutations(input))

    listt = []
    for i in l:
        listt.append(list(i))


    '''Brute Force'''
    for permutationnn in listt:
        print("Permutation to check: ",permutationnn)

        chess_board = create_chess_board(size_of_board)

        for index in range(size_of_board):

            chess_board[index][permutationnn[index]] = 1

        print(chess_board)

        # for col in range(len(permutationnn)):
        #     item = permutationnn[col]
        #     chess_board[col][item ] = 1


        print("Corresponding chess board: ",chess_board)

        a = check (chess_board, permutationnn, size)
        if a == True:
            print("True for permutation ", permutationnn)
            solutionss.append(permutationnn)
        print(a)

    print(time.time()-start_time)
    print(solutionss)

    return (solutionss)


if __name__ == "__main__":


    size_of_board = int(input("What is the size of the board?"))
    E_Queens(size_of_board)

