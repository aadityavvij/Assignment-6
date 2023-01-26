# 5. Write  a  Python  function  that  accepts  a  hyphen-separated  sequence  of  words  as  input 
#    and prints the words in a hyphen-separated sequence after sorting them alphabetically. 
#     Sample Items : green-red-yellow-black-white 
#     Expected Result : black-green-red-white-yellow

a = input("Enter hyphen-separated sequence\n")

def sequence(x):
    a1 = x.replace("-", " ")

    a2 = a1.split()

    a3 = sorted(a2)

    string = ""

    for i in a3:
        string = string + i + "-"

    print(string)

sequence(a)