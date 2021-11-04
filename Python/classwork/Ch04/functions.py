# basic function

#def message():
#    print("Welcome to North Tech!")

#message()

# basic function with 1 argument

#def myMessage(m,n):
#    print(m,n)

#name = "Tim"
#message = "Welcome to North Tech!"
#myMessage(message,name)

def area(length,width):
    area = int(length) * int(width)
    return area

length = input("What is the length? ")
width = input("What is the width? ")

rectArea = area(length,width)

print("The area is: "+ str(rectArea))
