# Built-in imports
import math
from re import U

# Your code below
GRADE = {}
for a in range(0,100+1):
    if a >= 70:
        GRADE[a] = "A"
    elif a >= 60:
        GRADE[a] = "B"
    elif a >= 55:
        GRADE[a] = "C"
    elif a >= 50:
        GRADE[a] = "D"
    elif a >= 45:
        GRADE[a] = "E"
    elif a >= 40:
        GRADE[a] = "S"
    elif a <40:
        GRADE[a] = "U"

def read_testscores(filename):
    """
    Adding each data as the values of the dictionary
    """
    data = open(filename, 'r')
    studentdata = []
    for i in data:
        i = i.strip().split(",")
        if i[2].isnumeric():
            overall = math.ceil((int(i[2])/30 * 15) + (int(i[3])/40 * 30) + (int(i[4])/80 * 35) + (int(i[5])/30 * 20))
            grade = GRADE[overall]
            student_dict = {'class':i[0],'name':i[1],'overall':overall,'grade':grade}
            studentdata.append(student_dict)
    data.close()
    return studentdata
        
    
def analyze_grades(studentdata):
    """
    Add each class to the full class_grade dictionary

    Add each grade as zero before running the loop so there is a nested dictionary for each grade as the value for each class

    run through the loop so that for each grade, the number of each grade increases by one

    class num is the key for each nested dictionary
    """
    class_grade = {}
    for i in studentdata:
        class_num = i['class']
        if class_num not in class_grade:
            class_grade[class_num] = {}
            grades = "ABCDESU"
            for a in grades:
                class_grade[class_num][a] = 0
        class_grade[class_num][i['grade']] += 1
    return class_grade

read_testscores("testscores.csv")