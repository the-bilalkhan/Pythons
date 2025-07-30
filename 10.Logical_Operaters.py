subject1_pass = True
subject2_pass = True

if subject1_pass and subject2_pass:
    print("You are passed your exam")

subject1_pass = True
subject2_pass = False

if subject1_pass or subject2_pass:
    print("You are passed but need improvement.")


subject1_pass = True
subject2_pass = False #Passed By grace marks

if subject1_pass and not subject2_pass:
    print("You are passed.")


