num1 = float(input( " Enter first number :"))
num2 = float(input( " Enter second number :"))
operation = input ( " Enter operation (+, -, *, /, : ")
if operation == "+" :
   result = num1 + num2
   print("result:" ,result)
elif operation == "-" :
     result = num1 - num2
     print("result:" ,result)
elif operation == "*" :
     result = num1 * num2
     print("result:" ,result)
elif operation == "/" :
     result = num1 / num2
     print("result:" ,result)
else :
     print("invalid operation!")
