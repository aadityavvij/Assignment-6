# 6. Write a Python function student_data () which will print the id of a student (student_id). 
#    If the user passes an argument student_name or student_class the function will print the 
#    student name and class. 

def studentInfo(student_id, student_name = None, student_class = None):
    print(student_id)
    print(student_name)
    print(student_class)

studentInfo(22103093)
print("\n")
studentInfo(22103093, 'Aaditya Vij', 'CSE')
