'''Aashish Adhikari 12:32 am 28 Sept. 2019'''
'''Define a function named factoring  that returns all prime factors of an integer. 
For example, factors(12) returns [2,2,3]. 
If the input is a prime or 1 it returns an empty list. 
The factors should be listed in increasing order. '''
import time, matplotlib.pyplot as plt


def factoring(original_inte):
    import math

    array_of_factors = []

    starting_time = time.time()

    if original_inte <= 0:
        print("Invalid input provided. Re-run with a positive integer input. Terminating the program.")
        return -1, time.time() - starting_time


    '''First divisor is 2 which is also the only prime factor , thus divide until 2 is able to divide to make the number odd'''

    while (original_inte % 2 == 0):
        array_of_factors.append(2)
        original_inte = original_inte / 2
        #print(str(original_inte) + "\t")

    # old code
    '''Now we will check only with odd numbers.'''
    odd_divisor = 3

    while original_inte > 1:
        while original_inte % odd_divisor == 0:
            array_of_factors.append(odd_divisor)
            original_inte /= odd_divisor

        '''After division fails, go to next odd number now.'''
        odd_divisor = odd_divisor + 2
        if odd_divisor > math.sqrt(original_inte):
            if original_inte > 1:
                array_of_factors.append(int(original_inte))
            break
    if len(array_of_factors) == 1:
        return [],time.time() - starting_time
    return array_of_factors, time.time() - starting_time

    '''The task requires to return an empty list if the input is a prime. That condition satisfies if the array_of_factors contains just one element.'''








if __name__ == "__main__":
    '''Single Input case'''
    #integer = input("Input an integer whose prime factors you want to list.")
    import math

    prime_factors_returned = []

    inputs_whose_prime_factors_we_need = []

    average_time_for_input = []
    input_size_in_no_of_digits = []

    #taking only specific values for the sake of curve fitting, else do from i = 1 to 1000000000
    for input in range(1,100000001,100000):


        prime_factors_returned, time_returned = factoring(input)



        average_time_for_input.append(time_returned)
        input_size_in_no_of_digits.append(math.log(input,2)) #if log of input as the input size
        #input_size_in_no_of_digits.append(input) # if the original input itself as the input size
        print(time_returned,input)

    print("The inputs were: ",inputs_whose_prime_factors_we_need)
    print("The time taken for all the inputs: ",average_time_for_input)
    plt.plot(input_size_in_no_of_digits,average_time_for_input)
    limit = 1



    # naming the x axis
    plt.xlabel('Input Size')
    # naming the y axis
    plt.ylabel('Average Running Time')
    # giving a title to my graph
    plt.title('Input size Vs Running time')
    # function to show the plot
    plt.show()









