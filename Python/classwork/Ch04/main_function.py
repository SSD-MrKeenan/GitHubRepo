def makeUser(fname,lname):
    username = fname+"."+lname
    return username.lower()


def main():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")

    username = makeUser(first_name,last_name)

    print("Your username is: "+username)

if __name__ == "__main__":
    main()
