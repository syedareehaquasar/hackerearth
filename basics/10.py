"""

Given two strings of equal length, you have to tell whether they both strings are identical.

Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2.

Input :

First line, contains an intger 'T' denoting no. of test cases.
Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.

Output:

For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.
String is made up of lower case letters.

SAMPLE INPUT
3
sumit mitsu
ambuj jumba
abhi hibb

SAMPLE OUTPUT
YES
YES
NO

"""


n = int(input())

arr1 = [0] * 26
arr2 = [0] * 26
for i in range(n):
    count = 0
    a, b = input().split()
    a = sorted(a)
    b = sorted(b)
    for j in range(len(a)):
        if a[j] is b[j]:
            count += 1

    if count is len(a):
        print("YES")
    else:
        print("NO")


"""
n = int(input())

arr1 = [0] * 26
arr2 = [0] * 26

for i in range(n):
    count = 0
    a, b = input().split()
    for j in a:
        arr1[ord(j) - ord('a')] += 1

    for j in b:
        arr2[ord(j) - ord('a')] += 1

    for j in range(26):
        if arr1[j] is arr2[j]:
            count += 1

    if count is 26:
        print("YES")
    else:
        print("NO")
"""