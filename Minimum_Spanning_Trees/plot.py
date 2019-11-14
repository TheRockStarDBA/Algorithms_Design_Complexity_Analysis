

import matplotlib.pyplot as plt
'''Kruskel'''
# N = [0.034, 0.036, 0.092, 0.244, 0.521 ]
# list= [4994,  19607,  49370, 140359, 315745]
'''Prim'''
list =[4994,  19607,  49370, 140359, 315745]
N = [0.022, 0.085, 0.255, 0.821, 1.987]
plt.plot(list,N)
# naming the x axis
plt.xlabel('No. of Edges')
# naming the y axis
plt.ylabel('Average Running Time')
# giving a title to my graph
plt.title('No. of Edges Vs Running time')
# function to show the plot
plt.show()
#
# test case 1 and 2:                 1000                                                     315745
#
# test case 3 and 4:                 1500                                                     140359
#
# test case 5 and 6:                 2000                                                     49370
#
# test case 7 and 8:                 1000                                                     19607
#
# test case 9 and 10:               1500                                                     4994