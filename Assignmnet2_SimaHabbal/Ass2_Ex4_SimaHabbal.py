names = ["Maria", "Hala", "Ghady", "Ehsan", "Joe", "Zoe"]
while True:
    letter = input("Enter a letter (or type 'quit' to exit): ")
    if letter.lower() == 'quit':
        break
    found_names = [name for name in names if letter.lower() in name.lower()]
    if found_names:
        print("Names containing the letter '{}':".format(letter))
        for name in found_names:
            print(name)
    else:
        print("No names contain the letter '{}'.".format(letter))
