import json

def print_filtered_users(filtered_users):
    if len(filtered_users) > 0:
        for user in filtered_users:
                print(user)
    else:
        print("No data found")

def filter_users_by_name(name):
    """ return users filtered by name """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["name"].lower() == name.lower()]
    #call the print filtered users function
    print_filtered_users(filtered_users)

def filter_by_age(age):
    """ return users filtered by age """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["age"] == age]

    # call the print filtered users function
    print_filtered_users(filtered_users)


def filter_by_email(email):
    """ return users filtered by email """
    with open("users.json", "r") as file:
        users = json.load(file)

    filtered_users = [user for user in users if user["email"] == email]

    # call the print filtered users function
    print_filtered_users(filtered_users)

if __name__ == "__main__":
    """ get user input to continue one of the filter """
    #while loop to keep asking and not drive to error in case wrong input
    while True:
        filter_option = input("What would you like to filter by? \nAvailable options: name, age, email: ").strip().lower()

        #filter by entered input conditions
        #between filter option input , try except to avoid error and stop the program.
        if filter_option == "name":
            name_to_search = input("Enter a name to filter users: ").strip()
            filter_users_by_name(name_to_search)
            break
        elif filter_option == "age":
            while True:
                try:
                    age_to_search = int(input("Enter an age (int number) to filter users: "))
                    filter_by_age(age_to_search)
                    break
                except ValueError:
                    print("Please enter int number")
            break
        elif filter_option == "email":
            email_to_search = input("Enter a email to filter users: ")
            filter_by_email(email_to_search)
            break
        else:
            print("> Filtering by that option is not yet supported. Please type from the existing options.")
            print() # add empty line