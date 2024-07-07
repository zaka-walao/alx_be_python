def perform_operation(num1:float,num2:float,operation):
    if operation == 'add':
        return num1+num2
    if operation == 'subtract':
        return num1-num2
    if operation == 'multiply':
        return num1*num2
    if operation == 'divide':
        if num2 == 0:
            return "Error: Cannot divide by zero"
        else:
            return num1/num2
    else:
        return "Error: Invalid operation"