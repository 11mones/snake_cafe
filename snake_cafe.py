print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************


""")
      
Appetizers = ["Wings" , "Cookies" , "Spring Rolls"]
Entrees =["Salmon" , "Steak" , "Meat Tornado" , "A Literal Garden"]
Desserts = ["Ice Cream" , "Cake" , "Pie"]
Drinks = ["Coffee" ,  "Tea" ,  "Unicorn Tears"]
print("Appetizers")
print("-------")
for x in Appetizers:
  print(x)
print("\n")
print("Entrees")
print("-------")
for x in Entrees:
  print(x)

print("\n")
print("Desserts")
print("-------")
for x in Desserts:
  print(x)

print("\n")
print("Drinks")
print("-------")
for x in Drinks:
  print(x)


print("""
***********************************
** What would you like to order? **
***********************************
""")
countList = []      
y = input(">")
countList.append(y)
# u = y.lower()

while (y.lower() != "quit"):


    if y.capitalize() in Appetizers:
      print("**",countList.count(y)," order of",y.capitalize(),"has been added to your meal**")
    elif y.capitalize() in Entrees:
        print("**",countList.count(y)," order of",y.capitalize(),"has been added to your meal**")
    elif y.capitalize() in Desserts:
        print("**",countList.count(y)," order of",y.capitalize(),"has been added to your meal**")
    elif y.capitalize() in Drinks:
        print("**",countList.count(y)," order of",y.capitalize(),"has been added to your meal**")       
    else :
      print("Sorry, we do not have this in the menu")  
    y = input(">")
    countList.append(y)
    

print("Thanks for using our app")

    