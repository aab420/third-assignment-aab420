'''
In this folder you will find a subfolder with a file "Data points.txt".
- The first column of the text file provides a list of 1000 points related to sensor 1
- The second column of the text file provides a list of 1000 points related to sensor 2

Write a program that extracts data from the file and computes the average 
of the two measurements (for each row, the average between sensor 1 and sensor 2). 
You will end up with 1000 data points that you need to write in another text file called "Data points average.txt"

Weight: 2
'''


import numpy as np

file = open("Data points.txt", "r")
text = file.read()
numbers = text.split()
total_list = list(numbers)
list_even = []
list_odd = []
list_averages = []
file2 = open("Data points average.txt","w")
for i, number in enumerate(total_list):
    if i % 2 == 0:
        list_even.append(float(number))
    elif i % 2 != 0:
        list_odd.append(float(number)) 
for i in list_even:
    for j in list_odd:
        average = (i+j)/2
        list_averages.append(average)
for k in list_averages:
    file2.write(str(k))
    file2.write("\n")
file2.close()
file.close()

"""
import numpy as np

file = open("Data points.txt", "r")
list_of_averages = []
list_of_lists = [(line.strip()).split() for line in file]

def averages(input_list):
    for i in input_list:
        list_of_averages.append((sum((i)/2)))
        # this line ^ definitely doesn't work
    i += 1
    return list_of_averages

ans = averages(list_of_lists)"""