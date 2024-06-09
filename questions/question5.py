# Question 5
# Python-Specific Questions:
# Question: Write a Python function that takes a list of integers and returns a new list containing only the even numbers from the input list.
def return_even(numbers):
    output = []
    for number in numbers:
        if number % 2 == 0:
            output.append(number)
    return output
# Code solution here
