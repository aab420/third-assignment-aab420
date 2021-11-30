'''
In this folder you will find a subfolder with a file "Data points.txt".
- The first column of the text file provides a list of 1000 points related to sensor 1
- The second column of the text file provides a list of 1000 points related to sensor 2

Write a program that extracts data from the file and plot them using matplotlib.pyplot.
The data relative to both sensors need to be plotted in the same graph (they are both relative to the y axis),
using different colors.
Add the following label to the x axis: "Time [s]"
Add the following label to the y axis: "Force [N]"

Weight: 2
'''
import matplotlib.pyplot as plt
file = open("Data points.txt", "r")
text = file.read()
numbers = text.split()
total_list = list(numbers)

sensor1_list = []
sensor2_list = []
for i, number in enumerate(total_list):
    if i % 2 == 0:
        sensor1_list.append(float(number))
    elif i % 2 != 0:
        sensor2_list.append(float(number))


time = [x for x in range(1000)] 
y = [a for a in sensor1_list]
y2 = [b for b in sensor2_list]
plt.plot(time, y, "r")
plt.plot(time, y2, "g")
plt.ylabel("Force [N]")
plt.xlabel("Time [s]")
plt.grid()
plt.show()




