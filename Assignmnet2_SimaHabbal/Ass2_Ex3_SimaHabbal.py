list1 = [54, 76, 2, 4, 98, 100]
while True:
    int1= input("Enter the first integer: ")
    int2= input("Enter the second integer: ")
    if int1.isdigit() and int2.isdigit():
        int1 = int(int1)
        int2 = int(int2)
        if int1 <= int2:
            valid_values = [value for value in list1 if int1 <= value <= int2]
            if valid_values:
                for value in valid_values:
                    print(value)
                break
            else:
                print("No values found in the specified range. Try again.")
        else:
            print("The first integer should be less than or equal to the second integer.")
    else:
        print("Invalid input. Please enter valid integers.")
