DAY = "Friday"

def displayMessage(greeting,weather):
    print(greeting)
    DAY = "Thursday"
    print("Today is " + DAY)
    print("It's " + weather + " outside.")

def main():
    w = "chilly"
    g = "Hello!"
    displayMessage(weather = w,greeting = g)
    print(DAY)


if __name__ == "__main__":
    main()
