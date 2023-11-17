#Sima Habbal
#i've chosen to create a list of all cities in lebanon, in order to validate cities
lebanese_cities = ["Akkar", "Tripoli", "Zgharta", "Koura", "Baalbek", "Jbail", "Kesrouan", "El Metn", "Zahle", "Beirut", "Aley", "Chouf", "Rachaya", "Hasbaya", "Jezzine", "Saida", "Nabatieh", "Marjaayoune", "Sour"]

def add_city(cities):
    city_name = input("Enter the name of the city: ").strip().capitalize()
# strip() Removes exess whitespaces from a string
#capitalize() firt letter capital and the rest lowercase
# isalpha() boolen checks if all characters are alphabetic
#isascii() checks if all characters in a string are ASCII
#make sure that the city name consists from letters, and compare it in lower case 
#make sure it does not exist in the companys cities list but does in the lebanese cities
    while not city_name.isalpha() or city_name.lower() in map(str.lower, cities) or city_name not in lebanese_cities:
        if not city_name.isalpha():
            print("Invalid city name. Please enter a valid name.")
        elif city_name.lower() in map(str.lower, cities):
            print("City already exists. Please enter a different name.")
        elif city_name not in lebanese_cities:
            print("City is not a valid Lebanese city. Please enter a valid name.")
        city_name = input("Enter the name of the city: ").strip().capitalize()

    cities.append(city_name)
  # sort() sorts a list in ascending order
    cities.sort()
    print(f"City '{city_name}' added successfully.")

def is_valid_name(name, drivers):
#isdigit() checks if all digits
#lower() lowers all the cases of letter
#make sure the name consists of only letters,has no spaces or other characters,and does not already exist in the drivers list
    return name.isalpha() and name.isascii() and not any(char.isdigit() or char.isspace() for char in name) and name.lower() not in map(str.lower, drivers)

def add_driver(drivers):
    driver_name = input("Enter the name of the driver: ").strip().capitalize()

    while not is_valid_name(driver_name, drivers):
        print("Invalid driver name. Please enter a valid name.")
        driver_name = input("Enter the name of the driver: ").strip().capitalize()
# split(',') splits a string into a list of substrings using a specified character
  
    if driver_name not in drivers:
        route = input("Enter the route for the driver (comma-separated cities): ").strip().split(',')
        route = [city.strip().capitalize() for city in route if city.strip().capitalize() in lebanese_cities]
#the lambda x: lebanese_cities.index(x) is a lambda function (anonymous function) 
#that returns the index of each element x in the lebanese_cities list.
#this is a new funtion to me
        route.sort(key=lambda x: lebanese_cities.index(x))
        drivers[driver_name] = route
        print(f"Driver '{driver_name}' added successfully with route: {route}")
    else:
        print(f"Driver '{driver_name}' already exists.")

def add_city_to_driver_route(drivers, cities):
    driver_name = input("Enter the name of the driver: ").strip().capitalize()
    if driver_name in drivers:
        city_name = input("Enter the name of the city to add: ").strip().capitalize()
        if city_name in cities:
            add_option = input("Enter 0 to add to the beginning, -1 to add to the end, or any other number to add to a specific index: ")
            try:
                index = int(add_option)
                if add_option == "0":
                    drivers[driver_name].insert(0, city_name)
                elif add_option == "-1":
                    drivers[driver_name].append(city_name)
                else:
                    drivers[driver_name].insert(index, city_name)
#in this method i didnt know it to sort or not, since the user is specifying the index of the city added
#ive decided not to sort it and leave it as the user chose
#the line below was supposed to sort the list but i will not be using it
#drivers[driver_name].sort(key=lambda x: lebanese_cities.index(x))
                print(f"City '{city_name}' added to the route of driver '{driver_name}' successfully.")
            except ValueError:
                print("Invalid index. Please enter a valid integer.")
        else:
            print(f"City '{city_name}' is not a valid city.")
    else:
        print(f"Driver '{driver_name}' not found.")

def remove_city_from_driver_route(drivers):
#remove any excess characters
#make sure the name of the driver is in dictionary drivers
#if the city exists in the drivers route it will be removed
    driver_name = input("Enter the name of the driver: ").strip().capitalize()
    if driver_name in drivers:
        city_name = input("Enter the name of the city to remove: ").strip().capitalize()
        if city_name in drivers[driver_name]:
            drivers[driver_name].remove(city_name)
            print(f"City '{city_name}' removed from the route of driver '{driver_name}' successfully.")
        else:
            print(f"City '{city_name}' is not in the route of driver '{driver_name}'.")
    else:
        print(f"Driver '{driver_name}' not found.")

def check_package_deliverability(drivers):
#check if the city is in any drivers' route
    city_name = input("Enter the name of the city for package delivery: ").strip().capitalize()
    delivering_drivers = [driver for driver in drivers if city_name in drivers[driver]]
    if delivering_drivers:
        print(f"The following drivers deliver to '{city_name}':")
        for driver in delivering_drivers:
            print(driver)
    else:
        print(f"No drivers deliver to '{city_name}'.")

def print_all_drivers(drivers):
    for driver, route in drivers.items():
        print(f"Driver: {driver}, Route: {route}")

def main():
    cities = ["Beirut", "Saida", "Sour"]
    drivers = {}

    while True:
        print("\nEnter:")
        print("1. To add a city")
        print("2. To add a driver")
        print("3. To add a city to the route of a driver")
        print("4. Remove a city from a driver’s route")
        print("5. To check the deliverability of a package")

        choice = input("Enter your choice (1-5, 0 to exit): ")

        if choice == "0":
            break

        if choice == "1":
            add_city(cities)

        elif choice == "2":
            add_driver(drivers)
            print_all_drivers(drivers)
        elif choice == "3":
            add_city_to_driver_route(drivers, cities)

        elif choice == "4":
            remove_city_from_driver_route(drivers)

        elif choice == "5":
            check_package_deliverability(drivers)


        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()
