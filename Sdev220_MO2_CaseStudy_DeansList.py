##This app will accept student names and GPAs and test if the student qualifies for either the Dean's List or the Honor Roll.
#App is asking for student to enter last name.
fisrstName = input("Please enter your first name: ")
#App asking for student's first name.
lastName = input("Please enter your last name: ")
fullName = (" ".join([fisrstName, lastName]))
#If else loop, if last name is zzz system willl quit, else, system will continue
if lastName == "zzz":
    quit()
else:
    print("Welcome back " + fullName )
 ##GPA loop, if gpa is => 3.5 student made it to the Dean's list, else he is an honor roll student.   
gpa = input (fullName + " Please enter your gpa: ")
score = float(gpa)
if score >= 3.5:
    print("Congratulations " + fullName + "," + " you have made the Dean's List")
else:
    if score <= 3.25:
       print(fullName + " you are an Honor Roll student")
    