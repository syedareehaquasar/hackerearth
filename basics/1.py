"""

You are given an integer N. You need to print the series of all prime numbers till N.

Input Format

The first and only line of the input contains a single integer N denoting the number till where you need to
find the series of prime number.

Output Format

Print the desired output in single line separated by spaces.

Constraints

1<=N<=1000

"""

n = int(input())

for num in range(n):
    if num > 1:
        for i in range(2, num):
            if num % i is 0:
                break
        else:
            print(num, end=" ")
