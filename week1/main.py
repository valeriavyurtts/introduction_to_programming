# name = input("enter your first name:")
# surname = input("enter your surname:")
# # print("Hello, " + name + "!")

# print(f"Hello, {name} {surname}!")

# WEEK 2

# User enters their age
# age = int(input("Enter your age: "))

# if (age > 18):
#     print("yes")
# elif (age == 26):
#     print("no")

# print("Hi, I help you understan, do you have enough money for new Iphone")


money = int(input("How much money for new Iphone you currently have?"))
if (money < 1000):
    print("Sorry, it still too early to buy a new phone.")
elif (money < 2000):
    print("Good, just a little more.")
elif(money < 3200):
    print("You almost there!")
else:
    print("You have enough money, Go to the store!!!")

