# Descrption: 

# This Student grade tracker project is based on python concepts : Dictionaries

def add_student(stud_data):
    stud_grade[stud_data[0]] = {}
    add_grades(stud_data[1:],stud_data[0])

def add_grades(stud_data,name):
    sub_names = stud_data[::2]
    marks = stud_data[1::2]
    if len(sub_names) == len(marks):
        for i in range(len(sub_names)):
            stud_grade[name][sub_names[i]] = marks[i]
    else:
        print("Data is insufficient")

def compute_gradeAvg(std_name):
    marks = [int(v) for v in stud_grade[std_name].values()]
    return sum(marks)/len(stud_grade[std_name])

def display_grade(std_name):
    try:
        print(stud_grade[std_name])
    except KeyError:
        print("Oops! No student is recorded with that name in our database.")
    
def get_topper():
    max = 0
    topper = None
    for i in stud_grade:
        score = compute_gradeAvg(i)
        if score > max :
            topper = i
            max = score
    print(f"Congratulations!!!  {topper} is topper with marks : {max}")

def get_failed_students_data():
    
    std_data = {}
    
    for i in stud_grade:
        std_data[i] = []
        for sub, marks in stud_grade[i].items():
            if int(marks) < 35:
               std_data[i].append(sub)
    failed_std_data = {k:v for k,v in std_data.items() if len(v)>0}
    
    return failed_std_data

if __name__ == "__main__":
    
    print("*********  Welcome to Student grade tracker  *********")
    print("Choose from ")
    print("1. Add student Details and grades")
    print("2. Display grades of student")
    print("3. Compute Average Grade of a student")
    print("4. Get topper Details and Score")
    print("5. Get failed students data")  
    print("6. Exit ")
    
    stud_grade = {}
    
    while True:
        
        try:
            choice = int(input("Enter your choice from Menu:"))
            if choice == 1:
                stud_data = input("Enter student data in this format: name,sub1,sub1_marks,sub2,sub2_marks...  :").split(",")
                add_student(stud_data)
            elif choice == 2:
                stud_name = input("Enter Student Name :")
                display_grade(stud_name)
            elif choice == 3:
                stud_name = input("Enter Student Name :")
                print(compute_gradeAvg(stud_name))
            elif choice == 4:
                get_topper()
            elif choice == 5:
                print(get_failed_students_data())
            elif choice == 6:
                print("Thank You.")
                break
            else:
                print("Invalid choice") 
                
        except ValueError:
            print("Invalid Value")
    