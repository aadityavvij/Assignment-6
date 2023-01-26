# 1. Write  a  Python  function  to  check  whether  a  number  is  perfect  or  not.  According to 
#    Wikipedia : In number theory, a perfect number is a positive integer that is equal to the 
#    sum of its proper positive divisors, that is, the sum of its positive divisors excluding the 
#    number  itself  (also  known  as  its  aliquot  sum).  Equivalently,  a  perfect  number is a 
#    number that is half the sum of all of its positive divisors (including itself).

a = int(input("Enter a number\n"))

def func(x):
    sum = 0

    for i in range(1, x):
        if (a%i==0):
            sum = sum + i
        else:
            pass

    if (sum==a):
        print(f"{x} is a perfect number")
    else:
        print(f"{x} is not a perfect number")

func(a)