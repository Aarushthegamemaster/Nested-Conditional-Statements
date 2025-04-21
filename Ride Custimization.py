print("1.Bike")
print("2.Car")
vehicle = int(input("Choose which vehicle you want by typing in the number:"))

if vehicle == 1:
    print("You have selected bike")
    print("Which type of bike you want")
    print("1.Scooty")
    print("2.Scooter")
    which_bike = int(input("Please enter the number of the bike you want:"))
    if which_bike == 1:
        print("You have selected Scooty")
        print("You ride is on the way!")
    elif which_bike == 2:
        print("You have selected Scooter")
        print("Your ride is on the way!")
    else:
        print("Invalid Input")
elif vehicle == 2:
    print("You have selected car")
    print("Which type of car you want")
    print("1.Sedan")
    print("2.XUV")
    which_car = int(input("Please enter the number of the car you want:"))
    if which_car == 1:
        print("You have chosen Sedan")
        print("Your ride is on the way!")
    elif which_car == 2:
        print("You have chosen XUV")
        print("Your ride is on the way!")
    else:
        print("Invalid Input")
else:
    print("Invalid Input")
  
