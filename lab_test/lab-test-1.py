# Azza Damia binti Khairul Zaman (C02)
# Lab test 1 : checks the grade for one student

def determine_grade (mark) : 
    if mark < 40 : 
        grade = "F"
    elif mark < 50 : 
        grade = "D"
    elif mark < 60 : 
        grade = "C"
    elif mark < 80 : 
        grade = "B"
    else : 
        grade = "A"
    
    return grade 

mark = float(input("Enter the student's mark : "))
grade = determine_grade(mark)
print ("Mark: " , mark)
print ("Grade: " , grade)