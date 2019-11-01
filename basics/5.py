"""

You have been given a positive integer N. You need to find and print the Factorial of this number. The Factorial of a positive integer N refers to the product of all number in the range from 1 to N. You can read more about the factorial of a number here.

Input Format:
The first and only line of the input contains a single integer N denoting the number whose factorial you need to find.

Output Format
Output a single line denoting the factorial of the number N.

SAMPLE INPUT
5

SAMPLE OUTPUT
120

"""

n = int(input())


def factorial(num):
    if num is 1:
        return 1
    else:
        return num * factorial(num-1)


print(factorial(n))


"""
n = int(input())
fact = 1

for i in range(1,n+1):
    fact *= i

print(fact)
"""