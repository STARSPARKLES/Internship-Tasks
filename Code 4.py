#Code 4
print("add for addition,sub for subtraction, mul for multiplication , div for division , mod for modulus") #provides a menu of options
while True:
    number_1=float(input("ENTER 1st NO: ")) #take input of 1st number 
    number_2=float(input("ENTER 2ND NO: ")) #take input of 2nd number 
    operation=input("WHAT TYPE OF OPERATION YOU WANT: ") #taking input what operation user want to perform from the menu options
    if operation=="add": # if operation is add
        addition= number_1+number_2 # adding two numbers and storing it in a addition variable 
        print(addition) #print addition result
    elif operation=="sub": #if operation is sub
        subtraction=number_1-number_2 # subtracting two numbers and storing it in a subtraction variable 
        print(subtraction) #print subtraction result
    elif operation=="mul": #if operation is mul
        multiplication=number_1*number_2  #subtracting two numbers and storing it in a multiplication variable 
        print(multiplication) #print multiplication result
    elif operation=="div": #if operation is div
        division=number_1/number_2 #dividing two numbers and storing it in a division variable 
        print(division) #print division result
    elif operation=="mod": #if operation is mod
        modulus=number_1%number_2  #divide two  numbers and storing remainder it in a modulus variable 
        print(modulus) #print modulus result
    else:
        print("this operation can't be performed" ) #if user enter other operation which is not in menu options it will print this statement
    repeat=input("DO YOU WANT TO PERFORM MORE OPERATIONS: ").lower() #if user want to perform more operations he/she say yes otherwise no save in repeat variable
    if repeat=='no':#if repeat value is no 
        break #it break the loop and end the program