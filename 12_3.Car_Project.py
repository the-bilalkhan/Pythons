command = ""
car_start = False

while True:
    command = input(">> ").lower()
    if command == "start":
        if car_start:
            print("Car Is Already Started.")
        else:
            car_start = True
            print("Car Started..")
    elif command == "stop":
        if not car_start:
            print("Car Already Stoped.")
        else:
            car_start = False
            print("Car Stoped..")
    elif command == "help":
        print('''
"start" for Start the car.
"stop" to stop the car.
"quit" to exit.
        ''')
    elif command == "quit":
        break
    else:
        print("Sorry.I don't Under Stand That.")