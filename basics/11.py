"""

Jack is your friend and Sophia is his girlfriend.
But due to some unknown reason ( unknown for us, they know it) Sophia started hating to Jack.
Now, Jack is in big trouble but he has a solution, He knows that if he will gift T patterns of a particular type
( For pattern observation see the sample test cases) then Sophia will start loving again to Jack.
But Jack is depressed now and need your help to gift her that type patterns of '*' and '#' of N lines.
So, it's your responsibility to save your friend's relationship.

Input :

First Line contains T i.e. number of test case.
Each of the next T lines contain an integer N.

Output:

For each test case print the pattern of N lines then after a blank line.

SAMPLE INPUT
3
9
2
5

SAMPLE OUTPUT
*################*
**##############**
***############***
****##########****
*****########*****
******######******
*******####*******
********##********
******************

*##*
****

*########*
**######**
***####***
****##****
**********

"""

n = int(input())
for i in range(n):
    a = int(input())
    for j in range(1, a + 1):
        for k in range(1, (2 * a) + 1):
            if j + 1 <= k <= 2 * a - j:
                print("#", end="")
            else:
                print("*", end="")
        print("")
    print("\n")

"""

n = int(input())
for i in range(n):
    a = int(input())
    m = a

    for j in range(a):
        print("*" * j,end="#" * m)
        print("")
        m -= 1
"""
