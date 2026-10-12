# Program to check whether a number is a palindrome

number = int(input("Enter a number: "))

original = number
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number = number // 10

if original == reverse:
    print("It is a palindrome")
else:
    print("It is not a palindrome")