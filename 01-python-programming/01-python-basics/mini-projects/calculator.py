## Ideas
# Calculator**: Take two numbers and an operator, then print the result.


number1=float(input("Enter first number: "))

number2=float(input("Enter second number: "))

operator=input("Enter operator (+, -, *, /): ")


if operator=="+":
    result=number1+number2
    print("Result:", result)
elif operator=="-":
    result=number1-number2
    print("Result:", result)
elif operator=="*":
    result=number1*number2
    print("Result:", result)
elif operator=="/":
    if number2!=0:
        result=number1/number2
        print("Result:", result)
    else:
        print("Error: Division by zero is not allowed.")

