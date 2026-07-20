"""
Fasly and truthy value  in python 
False

0

0.0

''

[]

{}

()

None

Everything else is considered True , generally truthy 

"""

if ""  or None:
    print("This will not print because the condition is False.")
elif 0   :
    print("This will not print because the condition is False. 1")
elif None :
    print("This will not print because the condition is False. abs")        
elif []  :
    print("This will not print because the condition is False. a")

elif {} or '&':   
    print("This will not print because the condition is False. $")    
elif () :
    print("This will not print because the condition is False.")
elif  0.0 :
    print("This will not print because the condition is False.")

elif False :
    print("This will not print because the condition is False.")

else:
    print("This will print because all previous conditions are False.")



"""
value_if_true if condition else value_if_false
"""   

result= "Even" if 4%2==0 else "odd"

print (result)


#  match cases

"""
match variable:

    case value1:
        ...

    case value2:
        ...

    case _:
        ...
"""
day=input("Enter a day of the week: ")
match day:
    case "Monday":
        print("Today is Monday.")
    case "Tuesday":
        print("Today is Tuesday.")
    case "Wednesday":
        print("Today is Wednesday.")
    case "Thursday":
        print("Today is Thursday.")
    case "Friday":
        print("Today is Friday.")
    case "Saturday":
        print("Today is Saturday.")
    case "Sunday":
        print("Today is Sunday.")
    case _:
        print("Invalid day.")




# Multiple Cases Together
day = "Saturday"

match day:

    case "Saturday" | "Sunday":
        print("Weekend")

    case "Monday" | "Tuesday":
        print("Weekday")

    case _:
        print("Other")        
