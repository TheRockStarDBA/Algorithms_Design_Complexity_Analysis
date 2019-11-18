import time, copy, statistics

def editDistance(string_A, string_B):
    '''returns the edit distance between the two input string and the edit string for converting string_A to string_B'''

    '''If we were not concerned about running time, we could have just done recursion frm the last string'''
    '''However, we want to use memoization and reduce the running time.'''
    '''So DP table.'''
    DP_table =  [ [0]*(len(string_A)+1) for i in range((len(string_B)+1))]
    DP_table[0][0] = 0
    edit_string = ""
    for col in range(0,len(string_A)+1):
        DP_table[0][col] = col
    for row in range(0,len(string_B)+1):
        DP_table[row][0] = row

    for row in range(1, len(string_B)+1):
        for col in range(1,len(string_A) + 1):

            left = DP_table[row][col - 1]
            up = DP_table[row - 1][col]
            diagonal = DP_table[row - 1][col - 1]
            minimum = min(up, left, diagonal)

            if col == row:
                if string_A[col-1] == string_B[row-1]:
                    edit_string = edit_string + '_'
                    DP_table[row][col] = minimum
                else:
                    edit_string = edit_string + 'R'
                    DP_table[row][col] = minimum + 1
            elif col > row:
                print string_A,string_B
                if string_A[col-1] == string_B[row-1]:
                    edit_string = edit_string + '_'
                    DP_table[row][col] = minimum
                else:
                    edit_string = edit_string + 'D'
                    DP_table[row][col] = minimum + 1
            else:
                if string_A[col-1] == string_B[row-1]:
                    edit_string = edit_string + '_'
                    DP_table[row][col] = minimum
                else:
                    edit_string = edit_string + 'I'
                    DP_table[row][col] = minimum + 1

    return (DP_table[len(string_B)][len(string_A)],edit_string)






if __name__ == "__main__":
    string_A = "BABBLE"
    string_B = "APPLE"
    edit_distance, edit_string = editDistance(string_A, string_B)
    print "The edit distance between ",string_A," and ",string_B," is ",edit_distance," and the edit string to convert ",string_A, " to ", string_B, " is ", edit_string,"."