#START
#ASK a user about current money savings 
#STORE the answer/input
# IF money(input) is less than 1000
#   DISPLAY "Sorry, it still too early to buy a new phone."
# ELSE IF money(input) is less than 2000
#   DISPLAY "Good, just a little more."
#ELSE IF money(input is less than 3200)
#   DISPLAY "You almost there!"
#ELSE 
#   DISPLAY "You have enough money, Go to the store!!!"
#END

print("Hi, I help you understand, do you have enough money for new Iphone")
money = int(input("How much money for new Iphone you currently have?"))
if (money < 1000):
    print("Sorry, it still too early to buy a new phone.")
elif (money < 2000):
    print("Good, just a little more.")
elif(money < 3200):
    print("You almost there!")
else:
    print("You have enough money, Go to the store!!!")
    