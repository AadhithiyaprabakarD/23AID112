# Level 3 Question 20

shopping_list = []

while(True):
    b = print("What to do ?")
    c = print(" Add or remove or show or quit ?")
    d = input()
    
    if(d == "add"):
        e = input("Enter the item name : ")
        shopping_list.append(e)
        print(e , " is added to the shopping list")
    elif(d == "remove"):
        f = input("Which item do you want to remove ?")
        if f in shopping_list :
            shopping_list.remove(f)
            print(f , " is removed from the shopping list ")
        else:
            print("Item not found ")
    elif (d == "show"):
        if len(shopping_list) == 0 :
            print("The current shopping list is empty ")
        else:
            print(shopping_list)
    elif(d == "quit"):
        print("Exiting ")
        break
    else :
        print("Invalid command . Try again !")

        
        
