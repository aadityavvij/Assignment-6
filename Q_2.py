# 2. Write a Python function that checks whether a passed string is palindrome or not. Note: 
#    A palindrome is a word, phrase, or sequence that reads the same backward as forward, 
#    e.g., madam or nurses run.

string = input("Enter a string\n")

def palindrome(x):
    newString = x.replace(" ", "")

    newStringInverted = newString[::-1]

    if newString==newStringInverted:
        print(f"{x} is a palindrome")
    else:
        print(f"{x} is not a palindrome")

palindrome(string)