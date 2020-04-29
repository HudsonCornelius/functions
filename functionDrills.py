'''
@author: amayamunoz
'''

'''
For this assignment you should read the task, then below the task do what it asks you to do.
For tasks with return statements, you can test out if you are correct by putting in some parameters
and printing what is returned outside of the function
EXAMPLE TASK:
'''
#EX) Define a function that adds two numbers and returns the result
def add_two_numbers(num1, num2):
    sumOfTwoNumbers = num1 + num2
    return sumOfTwoNumbers

'''
END OF EXAMPLE
'''

'''
START HERE
'''


#1) Define a function that subtracts the second number from the first number. Return the result.

def sub_two_numbers(num1, num2):
    subOfTwoNumbers = num1 - num2
    return subOfTwoNumbers


#2) Define a function that divides a number by 2, multiplies it by 77, and then adds 10000. Return the result.

def div_mult_add(num1):
    total = (num1 / 2) * 77 + 1000
    return total

#3) Define a function that checks if two numbers are equal. If they are equal, return true. If they are not equal, return false.

def equal_check(num1, num2):
    answer = (num1 == num2)
    return answer

#4) Define a function that takes in two numbers and returns the larger number. If they are the same, it should just return that number.

def largest_number(num1, num2):
    if num1 > num2:
        number = num1
    else:
        number = num2
    return number

#5) Define a function that takes in two words and returns a string that contains both words combined.

def word_combine(word1, word2):
    combination = word1 + word2
    return combination

#6) Define a function that takes in three numbers. If the first number is equal to the second OR the third number, return true. Else, return false.

def first_equal(num1, num2, num3):
    if (num1 == num2) or (num1 == num3):
        answer = True
    else: 
        answer = False
    return answer
    
#7) Define a function that prints your name.

def print_name(name):
    print(name)

#8) Define a function that takes in a string that is the name of a color. If that string is equal to your favorite color, it prints "That's my favorite color!" If it is not, it prints "That is not my favorite color. Try again."

def favorite_color(color):
    if color == "red":
        print("That is my favorite color!")
    else:
        print("That is not my favorite color, try again.")


#9) Define a function that takes in a number. If the number is not equal to zero, the function runs a loop until the number reaches 0. HINT: Within the loop, keep subtracting 1 from the number.

def number_zero(num):
    while(num > 0):
        num = num -1
    return num        
'''YOUR OWN FUNCTION'''

#10) Create your own function that solves any problem you can think of.

def square_number(num1):
    answer = num1 * num1
    return answer


