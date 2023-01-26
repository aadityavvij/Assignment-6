# 3. Write  a  Python  function  that  prints  out  the  first  n  rows  of  Pascal's  triangle.

k = int(input("Enter the value of n\n"))

def pascalTriangle(n):
    space = " "
    for i in range (1, n+1):
        if i==1:
            a = "1 "
            print((space*(n-i)) + a)
        elif i==2:
            a4 = "11"
            a_ = "1 1 "
            print((space*(n-i)) + a_)
        else:
            # a1 = ""
            a2 = ""
            a3 = ""
            for j in range(0,i-2):
                a1 = str(int(a4[j]) + int(a4[j+1]))
                a2 = a2 + a1 + space
                a3 = a3 + a1
            a = "1" + a3 + "1"
            a_ = "1 " + a2 + "1"
            a4 = a_.split()
            print((space*(n-i)) + a_)
# include (space*(n-i)) + a_ for triangle pattern

pascalTriangle(k)
