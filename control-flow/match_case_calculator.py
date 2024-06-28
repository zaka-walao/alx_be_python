num1 = float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
operation = input("Choose the operation (+, -, *, /): ")

match operation :
    case "+" :
        result = num1 + num2
    case "-" :
        result = num1 - num2
    case "*" :
        result = num1 * num2
    case "/" :
        if  num2 != 0 : 
            result = num1 / num2
        else : 
            print("Cannot divide by zero.")
    case _ :
        print("Invalid day entered.")

print(f"The result is {result}.")