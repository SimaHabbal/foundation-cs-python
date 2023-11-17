while True:
    num=input("Enter a number:").strip()
    if(num.isdigit()):
        num=int(num)
        digit=len(str(num))
        print(f"{num} has {digit} digits.")
        break
    else:
        print("Invalid Inpit. Please enter an integer.1234")