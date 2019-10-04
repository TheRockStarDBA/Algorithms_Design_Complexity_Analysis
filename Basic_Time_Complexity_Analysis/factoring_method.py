def factoring(original_inte):
    import math, time

    array_of_factors = []

    starting_time = time.time()

    if original_inte <= 0:
        print("Invalid input provided. Re-run with a positive integer input. Terminating the program.")
        return -1

    '''First divisor is 2 which is also the only prime factor , thus divide until 2 is able to divide to make the number odd'''

    while (original_inte % 2 == 0):
        array_of_factors.append(2)
        original_inte = original_inte / 2
        # print(str(original_inte) + "\t")

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
        return []
    return array_of_factors
