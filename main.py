print("Welcome to the Student Grading System!")
print()

while True:
    name = str(input("Enter student name: "))

    # I'm ensuring that number between 0 and 100, and validating it, this is test1 variable
    test1 = int(input("Enter score for Test 1 (0-100): "))
    while test1 < 0 or test1 > 100:
        print()
        test1 = int(input("Please, enter a number between 0 and 100 for Test 1: "))

    # test2
    test2 = int(input("Enter score for Test 2 (0-100): "))
    while test2 < 0 or test2 > 100:
        print()
        test2 = int(input("Please, enter a number between 0 and 100 for Test 2: "))

    # test3
    test3 = int(input("Enter score for Test 3 (0-100): "))
    while test3 < 0 or test3 > 100:
        print()
        test3 = int(input("Please, enter a number between 0 and 100 for Test 3: "))

    # Storing values for clearly looking code
    average = float((test1 + test2 + test3) / 3)
    # Rounding to the 2 numbers after point
    average = int(average * 100) / 100

    if average >= 90:
        grade = 'A'
    elif average >= 80:
        grade = 'B'
    elif average >= 70:
        grade = 'C'
    elif average >= 60:
        grade = 'D'
    else:
        grade = 'F'

    # Displaying data
    print()
    print("Calculating results...")
    print(f"Student: {name}")
    print(f"Test Scores: {test1}, {test2}, {test3}")
    print(f"Average: {average}")
    print(f"Grade: {grade}")
    print()

    # Asking for continuity, and checking value
    is_continuing = str(input("Do you want to enter another student's details? (yes/no): "))

    if is_continuing == 'yes':
        print()

    if is_continuing == 'no':
        print()
        print("Thank you for using the Student Grading System. Goodbye!")
        break