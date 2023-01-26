# 4. Write a Python function to check whether a string is a pangram or not. Note: Pangrams 
#    are  words  or  sentences  containing  every  letter  of  the  alphabet  at  least  once.  For 
#    example: "The quick brown fox jumps over the lazy dog"

l = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

string1 = (input("Enter a string\n")).lower()

def pangram(string):
    l1 = []
    for i in string:
        l1.append(i)

    for j in l:
        if j in l1:
            pass
        else:
            print("It is not a pangram")
            quit()
    print("It is a pangram")

pangram(string1)