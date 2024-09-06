# Function to find the largest of three integers
def find_largest(num1, num2, num3):
    # Check if num1 is larger than both num2 and num3
    if num1 >= num2:
        if num1 >= num3:
            return num1
        else:
            return num3
    else:
        # If num1 is not larger than num2, check if num2 is larger than num3
        if num2 >= num3:
            return num2
        else:
            return num3

# Get user input for three integers
try:
    number1 = int(input("Enter the first integer: "))
    number2 = int(input("Enter the second integer: "))
    number3 = int(input("Enter the third integer: "))

    # Find and print the largest number
    largest = find_largest(number1, number2, number3)
    print(f"The largest number is: {largest}")

except ValueError:
    print("Please enter valid integers.")
