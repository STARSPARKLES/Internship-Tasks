#Code 2
print("enter celsius or c for celsius and enter fahrenheit or f for fahrenheit") #specifying appropriate words for unit measurement that a user should enter
temperature=float(input("ENTER TEMPERATURE: "))#taking input of temperature
unit_measurement=input("CELSIUS(C) OR FAHRENHEIT(F)?: ") #taking unit input
unit_measurement=unit_measurement.lower() #make unit into lower case
if unit_measurement=="fahrenheit" or unit_measurement=="f": #if unit is 'fahrenheit' or 'f'
    celsius_result= 5/9*(temperature-32) #convert fahrenheit into celsius
    print(f"Fahrenheit to Celsius {celsius_result:.2f}°C") #print celsius_result upto  2 decimal places
elif unit_measurement=="celsius" or  unit_measurement=="c" : #if unit is 'celsius' or 'c'
    fahrenheit_result=(9/5*temperature)+32  #convert celsius into fahrenheit
    print(f"Celsius to Fahrenheit {fahrenheit_result:.2f}°F") #print fahrenheit_result upto  2 decimal places
else:
    print("Invalid unit") #print invalid