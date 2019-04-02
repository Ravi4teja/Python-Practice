#Average of given numbers

number1 = input("Enter the first number?\n>")
number2 = input("Enter the second number?\n>")

print("Type of entered number1 is", type(number1))
print("Type of entered number2 is", type(number2))
try:
	num1 = int(number1)  #Converting input to string
	num2 = int(number2)


	print("After converting inputs to integers using built_in function int()")
	print("Type of entered num1 is", type(num1))
	print("Type of entered num2 is", type(num2))

	avg = (num1 + num2)/2
	print("Average of the two numbers is", avg)
except:
	print("Please provide integers to perform average")


