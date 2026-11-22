try:
    number=int(input("Enter a number:"))
    result=100/number
    print("Your answer:", result)
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Number cannot be zero.")


try:
    age=int(input("Enter you age:"))
    if age>=1 and age<=100:
        print("Valid age")
    else:
        print("Invalid age")
except ValueError:
    print("Age should be a numeral.")









name="Shivam"
age=27

print(int("Hello"))






