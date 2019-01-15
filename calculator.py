x = int(raw_input("Enter the value for x: "))
print x

y = int(raw_input("Enter the value for y: "))
print y

operation = raw_input("Choose math operation (+, -, *, /): ")
print operation

if operation == "+":
    print x + y

elif operation == "-":
    print x - y

elif operation == "*":
    print x * y

elif operation == "/":
    print  x / y

else:
    print "You did not choose correct math operation"
