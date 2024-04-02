#Code 3
import re
regular_expression=re.compile(r"^(?!^\.+-_)[a-zA-Z0-9]+[+-.]?[a-zA-Z0-9_]*@[a-zA-Z]+\.[a-zA-Z]{1,}$") #regular expression that validates email
email_input=input('ENTER EMAIL: ') #taking input email
valid=regular_expression.match(email_input) #checking whether email is valid or not 
if valid is not None: # if valid variable is not None
    print("VALID EMAIL") #print email is valid
else: #if it is None
    print("INVALID EMAIL") #print invalid email
    