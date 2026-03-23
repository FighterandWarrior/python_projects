#!usr/bin/python3

# start - running the code 
#1: print/display options and ask for input
# 2: take input and run through loops to determind what to do?
# 3: if 1 = append to the list
# 4: if 2 = ask for which item to delete, input nr of item, vertify nr, and delete item from list, then reload list and return to start.
#5: load the list and display it.
#6: exit. exit the program 


toDo = []

#list_File = open('List.txt', 'x')

print("To Do")
print("======")
print("What would you like to do? \n 1) Add to list \n 2) Remove from list \n 3) Show list \n 4) Exit \n ")

answer = input("Your pick: ")
        
if answer == '1':
    newItem = input()
    toDo.append(newItem)
    print(toDo)

if answer == '2':
    print(toDo)
    deleteItem = input()
    toDo.remove(deleteItem)
    print(toDo)
    
       
if answer == '3':
    print(toDo)
        
    

