#creating a simple calculator to ask for user input and perform basic arithmetic operations

#defining variables
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

#performing calculations
sum = num1 + num2
difference = num1 - num2
product = num1 * num2
division = num1 / num2
# checking for division by zero

print("Results:")
print("Sum:", sum)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
