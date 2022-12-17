display="""  
            Sunway grading System
            Maitedevi , KTM
            """

def initialDisplay():
    print(display)

def inputInformation():
    name=input("Enter your name")
    address=input("Enter your Address")
    gmail=input("Enter your gmail")
    rollno=input("Enter your Roll.No")
    math,science,psychology,python,Java=[ int(x) for x in input("Enter your percentageof math,science,psychology,python,Java ").split()]
    totalMarks=math + science + psychology + python + Java
    initialDisplay()
    grade=calculateGrade(totalMarks)
    displayInformation(name,address,gmail,rollno,grade)

def calculateGrade(totalMarks):
    grade=""
    percentage=(500/totalMarks) * 100
    if(percentage>90 and percentage<=100):
        grade="A+"
        print("Your grade is A+")
        return grade
    elif(percentage>80 and percentage<=90):
        grade="A"
        print("Your grade is A")
        return grade
    elif(percentage>70 and percentage<=80):
        grade="B+"
        print("Your grade is B+")
        return grade
    elif(percentage>60 and percentage<=70):
        grade="B"
        print("Your grade is B")
        return grade
    elif(percentage>50 and percentage<=60):
        grade="C+"
        print("Your grade is C+")
        return grade
    elif(percentage>40 and percentage<=50):
        grade="C"
        print("Your grade is C")
        return grade
    else:
        grade="Fail"
        print("You are fail")
        return grade

def  displayInformation(name,address,gmail,rollno,grade):
    print("Name :"+ name)
    print("Address: "+ address)
    print("Gmail: " + gmail)
    print("RollNo: "+rollno)
    print("Grade:"+grade)

inputInformation()