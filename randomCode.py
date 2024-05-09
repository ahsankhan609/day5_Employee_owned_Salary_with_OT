"""This function takes in a number and prints "Fizz" if the number is divisible by 3, "Buzz" if the number is
divisible by 5, or "FizzBuzz" if the number is divisible by both 3 and 5. If the number is not divisible by 3 or 5,
the function prints the number itself.

Parameters:
- number (int): The number to be checked.

Returns:
- None
"""


def fizz_buzz(number):
    # Initialize an empty string to hold the result
    result = ""

    # Check divisibility by 3 and 5 and concatenate the appropriate strings
    if number % 3 == 0:
        result += f"{number} (Fizz), It is divisible by 3."
    if number % 5 == 0:
        result += f"{number} (Buzz), It is divisible by 5."

    # If the result is still empty, the number is not divisible by 3 or 5
    if not result:
        result = str(number) + " Can't be dividend by 3 or 5."

    # Print the result
    print(result)


# Example usage:
for i in range(1, 51):
    fizz_buzz(i)
