# different ways creating string
# my_string = 'hello'
# print(my_string)
# my_string = "hello"
# print(my_string)
# my_string = '''hello'''
# print(my_string)
# my_string = """hello, welcome to the world python"""
# print(my_string)

# concatenating two strings using + operator
# str1="hello"
# str2="world"
# print ("string 1:",str1)
# print ("string 2:",str2)
# str=str1+str2
# print("concatenated two different strings:",str)

# finding the length of the string
# str = "teju"
# print(len(str))

# extract a string using substring
# string = "teju reddy"
# print(string[0:5])

# searching in strings using index
# ch = "geeks for geeks"
# ch1 = "geeks"
# pos = ch.index(ch1,2)
# print ("the first position of geeks after 2nd index : ", end="")
# print (pos)

# matching a string against a regular expression with matches
# import re
# heroregex = re.compile (r'batman|tina fey')
# mo1 = heroregex.search('batman and tina fey.')
# print(mo1.group())

# comparing strings
# name = 'Teju'
# name2 = 'teju'
# name3 = 'Bely'
# name4 = 'bely'
# print("are name and name 1 equal?")
# print(name == name2)
# print("are name and name3 different?")
# print(name != name3)
# print("is name less than or equal to name2?")
# print(name <= name2)
# print("is name3 grater than or equal to name2?")
# print(name3 >= name2)
# print("is name4 less than name?")
# print(name4 < name)

# startswith(), ends with(), and compare to()
# str = "geeksforgeeks"
# print(str.startswith("geeks"))
# print(str.startswith("geeks", 4, 10))
# print(str.startswith("geeks", 8, 14))
# print("\n")
# print(str.endswith("geeks"))
# print(str.endswith("geeks", 2, 8))
# print(str.endswith("for", 5, 8))

# trimming strings with strip()
# greeting = "    hello!   "
# stripped_greeting = greeting.strip()
# print(greeting,"how are you?")

# replacing characters in strings wih replace()
# string = "teju for teju teju teju teju"
# print(string.replace("teju", "Teju"))
# print(string.replace("teju", "TejuforTeju", 3))

# splitting strings with split()
# text = 'geeks for geeks'
# print(text.split())
# word = 'geeks, for, geeks'
# print(word.split(','))
# word = 'geeks:for:geeks'
# print(word.split(':'))
# word = 'catbatsatfator'
# print(word.split('t'))

# converting integer objects to strings
# integer_year = 2022
# string_year = str(2022)
# print("this is " + string_year + ".")
# print(str())

# converting to uppercase and lowercase
# string = "I AM TEJU."
# print(string.swapcase())
# string = "i am teju."
# print(string.swapcase())
# string = "I aM tEjU."
# print(string.swapcase())