#GPA Calc.

#Lists.
classes= []
grades = []

#n is the number of classes (integer) the student wants to calculate.
n = int(input("How many classes are you enrolled in? "))
#Collects the necessary strings and grades in letter form.
#Def defines the start of a new function.

def collect():
    #i is depenedent on the integer n.
    for i in range(n):
        #the classname will be collected then the append (which means 'attach') will associate the class name with the amount of classes and then list it.
        className = input("Enter Class Name: ")
        classes.append(className)
    #'classes' is a list as defined on line 4.
    print(classes)

    #we are still in the range of integer n.
    for i in range(n):
        #same concept as the string in def colect, except now we are collecting letter grades for each defined class.
        grade = input("Enter Your Grade For Each Class Listed in Order (Letter Form): ")
        #.upper() makes all previous inputs upper case.
        grade = grade.upper()
        grades.append(grade)

    calculate()
#collects and initates caluclations
def calculate():
    #letter grades inputted above will be associate with this grade key referenced from UC's website.
    grade_key = {
        'A': 4,
        'A-': 3.6667,
        'B+': 3.3333,
        'B': 3,
        'B-': 2.6667,
        'C+': 2.3333,
        'C': 2,
        'C-': 1.6667,
        'D+': 1.3333,
        'D': 1,
        'D-': .6667,
        'F': .0000,
        # ... and so on
    }
    total = 0
    #The code takes grades and associates the letter grade with the respected grade point.
    for grade in grades:
        #total is 0 and += adds the grade point association(s) to the previously defined intial 0.
        total += grade_key[grade]
    #divide by the defined 'n' from line 8.
    gpa = total / n
    #prints string then calculated gpa.
    print("Your current standing semester gpa is ",gpa)

#defined variable for the def collect function prior.
collect()
