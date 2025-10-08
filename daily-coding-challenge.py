# Language Used - Difficulty of 1-10

# ===================
# October 10/8/25

# Python - 2
# def remove_duplicates(user_input):
#     new_list = [x for x in user_input.split(",")]
#     final_list = []

#     for i in new_list:
#         if i in final_list:
#             continue
#         else:
#             final_list.append(i)
#     result = final_list
#     return result

# user_input = input("Enter here: ")
# print(remove_duplicates(user_input))


# Python - CP2 Lab 1 Midterm
user_input = (input("Enter a number to convert to binary.\nInput: "))
num = int(user_input) # Converts the string input to int as instructed
list = [] # List to store each binary digit

# Loops until num reaches 0
while num > 0:
    # Detects if num has a remainder and stores 1 or 0 inside the list accordingly
    remainder = num % 2 
    if remainder == 0:
        list.append("0")
    else:
        list.append("1")

    # Divides the num
    num = num // 2

reversed = list[::-1] # Reverses the list so that it starts from the last
result = "".join(reversed)
print(f"Output: {result}")


# ===================
# October 10/6/25

# Python - 3
# def fizzbuzz(n):
#     result = []
#     for i in range (1, n+1):
#         if i%3 == 0 and i%5 == 0:
#             result.append("FizzBuzz")
#         elif i%3 == 0:
#             result.append("Fizz")
#         elif i%5 == 0:
#             result.append("Buzz")
#         else:
#             current_num = str(i)
#             result.append(current_num)
#     return result

# n = int(input("Enter here: "))
# print(fizzbuzz(n))


# ===================
# October 10/4/25

# Python - 1
# def is_even(integer):
#     if integer % 2 == 0:
#         result = True
#     else:
#         result = False
#     return result

# integer = int(input("Enter here: "))
# print(is_even(integer))


# ===================
# October 10/1/25

# Python - 4
# def find_missing_number(list):
#     int_list = [float(x) for x in list.split(",")]

#     n = max(int_list)
#     expected_sum = n * (n + 1) / 2
#     actual_sum = sum(int_list)

#     result = expected_sum - actual_sum
#     return result

# list = str(input("Enter here, separate each number by a comma: "))
# print(find_missing_number(list))


# Python - 2
# def find_largest(num):
#     largest = num[0]

#     for current_num in num:
#         if largest >= current_num:
#             largest = largest
#         else: 
#             largest = current_num
#     result = largest
    
#     return result

# user_input = str(input("Enter numbers separated by a comma: "))
# num = [float(x) for x in user_input.split(",")]

# print(find_largest(num))


# ===================
# September 9/30/25

# Python - 3
# def is_palindrome(string):
#     if string == " ":
#         result = True
#     else:
#         updated_string = string.lower().replace(".","").replace("!","").replace(",","").replace(";","").replace("?","").replace(":","").replace('"',"").replace("'","").replace("(","").replace(")","").replace(" ","").replace("/","")
#         reversed_string = updated_string[::-1]
#         if updated_string == reversed_string:
#             result = True
#         else:
#             result = False

#     return result


# string = str(input("Enter a sentence here: "))
# print(f"Palindrome: {is_palindrome(string)}")


# ===================
# September 9/27/25

# Python - 3
# def count_words (sentence):
#     sentence1 = sentence.replace(".","").replace("!","").replace(",","").replace(";","").replace("?","").replace(":","").replace('""',"").replace("''","").replace("()","")
#     sentence2 = sentence1.lower().split()
#     word_count = {}

    
#     for word in sentence2:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1

#     return word_count

# sentence = str(input("Enter a sentence: "))
# print(count_words(sentence))


# ===================
# September 9/26/25z

# Python - 1
# def celcius_to_fahrenheit(celsius):
#     fahrenheit = (celsius * 9 / 5) + 32
#     return fahrenheit

# celsius = float(input("Enter the Celsius degree here: "))
# conversion = celcius_to_fahrenheit(celsius)
# print(f"Its Fahrenheit equivalent is {conversion}!")


# # Python - 2
# def simple_calculator(num1, num2, operation):
#     if operation == "add":
#         result = num1 + num2
#     elif operation == "subract":
#         result = num1 - num2
#     elif operation == "multiply":
#         result = num1 * num2
#     elif operation == "divide":
#         result = num1 // num2
#     else:
#         print("You can only choose between 'add', 'subtract', 'multiply', and 'divide' as its operator.")
#     return result

# num1 = float(input("\nEnter first number: "))
# num2 = float(input("Enter second number: "))
# operation = str(input("Operations available: 'add' 'subtract' 'multiply' 'divide'\nEnter chosen operation: "))
# answer = simple_calculator(num1, num2, operation)

# print(f"Answer: {answer}")










