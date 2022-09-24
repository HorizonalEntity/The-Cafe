print("Welcome to Horizon Bakery!")
name = input("What is your name?\n")
print("Hello, " + name + "! how may we help you today?\n\n\n")

menu1 = "Bakery Items: Sandwich Bread, Donut, Hot Dog,Pizza.\n"
menu2 = "Drinks: Coffee, Latte, Cappuccino, Green Tea,Chocolate Milk, Orange Juice."

print("Here is what we have in our menu:\n" + menu1 + menu2)
order = input("What would you like to order?\n")

price = 5

quantity = input("how many would you like?\n")
total = price * int(quantity)

print("Your order has been placed: " + quantity + " " + order + "s")
print("Your total: $" + str(total))

confirmation = input("Would you like to confirm? (y/n)\n")

if confirmation == "y":
  print("Thank you! we'll have those " + order + "s " + "ready in a minute!")
  print("You claimed your order.")
elif confirmation == "n":
  print("Your order has been cancelled. please re-run the code to do it again!")