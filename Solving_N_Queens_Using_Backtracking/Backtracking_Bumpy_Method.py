'''Not written by me from scratch. This method of coding is too neat .'''

def B_Queens(size):


    rows = size
    columns = size
    solutions = [[]]

    for row in range(0,rows):
        solutions = next_column(row, columns, solutions)
    return solutions



def next_column(another_row, cols, last_answers):

    return [solution + [new_column]
            for solution in last_answers
            for new_column in range(cols)
            if no_attack(another_row, new_column, solution)]



def no_attack(new_row, new_column, solution):
    return all(solution[row]       != new_column           and
               solution[row] + row != new_column + new_row and
               solution[row] - row != new_column - new_row
               for row in range(new_row))

