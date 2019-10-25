

import matplotlib.pyplot as plt
N = [4,5,6,7,8]
list= [0.000087165, 0.0047461, 0.029964923, 0.2390158, 2.228800]

plt.plot(N,list)
# naming the x axis
plt.xlabel('No. of Queens')
# naming the y axis
plt.ylabel('Average Running Time')
# giving a title to my graph
plt.title('No. of Queens Vs Running time')
# function to show the plot
plt.show()