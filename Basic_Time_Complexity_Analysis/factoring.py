'''Aashish Adhikari 12:32 am 28 Sept. 2019'''
'''Define a function named factoring  that returns all prime factors of an integer. 
For example, factors(12) returns [2,2,3]. 
If the input is a prime or 1 it returns an empty list. 
The factors should be listed in increasing order. '''
import time

def factoring(original_int):

    array_of_factors = []
    '''A number cannot be divisible by another number larger than its half. Hence we will run the loop until int/ 2'''

    int = original_int

    '''First divisor is 2, thus divide until 2 is able to divide to make the number odd'''
    while (int % 2 == 0):
        array_of_factors.append(2)
        int = int/ 2

    odd_divisor = 3


    while (int <= original_int):#even though we need to check only upto half the value of original integer, doing <= original integer to satisfy logic here

        while (int % odd_divisor == 0):
            array_of_factors.append(odd_divisor)
            int = int / odd_divisor

        odd_divisor = odd_divisor + 2

        '''Stop after reaching and using the largest prime divisor.'''
        if int == 1:
            break


    '''Sort the items and return the list of factors'''
    array_of_factors.sort()
    return array_of_factors

if __name__ == "__main__":

    integer = input("Input an integer whose prime factors you want to list.")
    prime_factors = factoring(integer)
    print("The prime factors of "+ str(integer) + " are " + str(prime_factors) + ".\n")





