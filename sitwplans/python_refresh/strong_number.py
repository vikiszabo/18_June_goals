'''
Strong number is the number that the sum of the factorial of its digits is equal to number itself.
1! + 4! + 5! = 1 + 24 + 120 = 145
So, 145 is a Strong number.
Given a number, Find if it is Strong or not.
Number passed is always Positive .
Return the result as String
1- strong_num (1)  ==> return "STRONG!!!!"
'''

import math

def tell_if_strong(number):
    num = str(number)
    digits = []
    for n in num:
        digits.append(n)

    fact = 0
    for d in range(0, len(digits)):
        numb = int(digits[d])
        fact += math.factorial(numb)
    if fact == number:
        return "Strong!!!"
    else:
        return "Not Strong!!!"


szam = 150

print(tell_if_strong(szam))

def strong_num(number):
    return "STRONG!!!!" if sum(math.factorial(int(i)) for i in str(number)) == number else "Not Strong !!"