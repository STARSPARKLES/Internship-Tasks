#Code 5
def palindrome():#palindrome function
    string=input("ENTER STRING") #taking string input
    reversed_string=''.join(reversed(string)) #using reversed() function on string alphabets and then join these alphabets back into string 
    if reversed_string==string: #checking revserse string is equal to string
      return  print(f"This word '{string}' is a palindrome") #print it is a palindrome
    else: #if reverse string not equal to string 
      return  print(f"This word '{string}' is not a palindrome") #print it is not a palindrome
palindrome() #calling function