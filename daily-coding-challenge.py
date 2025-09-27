# Language Used - Difficulty of 1-10

# ===================
# September 9/26/25

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


# ===================
# September 9/27/25

# Python - 3
def count_words (sentence):
    sentence1 = sentence.replace(".","").replace("!","").replace(",","").replace(";","").replace("?","").replace(":","").replace('""',"").replace("''","").replace("()","")
    sentence2 = sentence1.lower().split()
    word_count = {}

    
    for word in sentence2:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    return word_count

sentence = str(input("Enter a sentence: "))
print(count_words(sentence))


# ===================
