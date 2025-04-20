medic_cond = str(input("Do you have a medical condition, Yes or No:"))
atendance = int(input("Please enter the student's attendance:"))

if medic_cond == "Yes":
    print("You are allowed")
else:
    if atendance>=75:
        print("You are allowed")
    else:
        print("You are not allowed")