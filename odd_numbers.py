# Print each odd number between 1 and 10 inclusive. 
# Hint - you will need to use the modulus operator % to determine whether a number is odd or even.

for number in range(1,11):
    if number % 2 != 0:
        print(number)