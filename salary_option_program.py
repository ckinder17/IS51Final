""" STRUCTURED ENGLISH
We will be writing a program that displays the number of final grades, the average grade, and the percentage of grades that are about the average grade.
We will write a main() funcrion to initialize (kickstart) the application, and a calculate_percentage_above_average() function to calculate the percentage
of grades that are above the average grade.
Open the file "Final.txt" to get the information and then close the file.
We then need to average the grades (sum of grades/number of grades)
If the grade is above average, += 1
Print the number of grades, the average grade, and then the percentage of grades above average.
The number of grades is 24, the average grade is 83.25%, and the percentage of grades above average is 54.17%.
"""

""" PSEUDOCODE

open final.txt infile
grades = line infile
close infile
average = sum(grades) / number(grades)

for grade in grades:
    if grade is above average
        add 1
print("Number of grades:", number of grades)
print("Average grade:", sum of grades / number of grades)
print("Percentage of grades above average: % above average)

"""