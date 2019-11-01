"""
Given two strings, a and b , that may or may not be of the same length, determine the minimum number of character deletions required to make a and b anagrams. Any characters can be deleted from either of the strings.

Input :

test cases,t
two strings a and b, for each test case
Output:

number of alphabets need to be removed

Note :

Anagram of a word is formed by rearranging the letters of the word.

For e.g. -> For the word RAM - MAR,ARM,AMR,RMA etc. are few anagrams

SAMPLE INPUT
1
cde
abc

SAMPLE OUTPUT
4

"""

t = int(input())
arr1 = []
result = 0
arr3 = []
for i in range(t):
    a = input()
    b = input()

    arr1 = [0] * 26

    for j in a:
        arr1[ord(j) - ord('a')] += 1

    for k in b:
        arr1[ord(k) - ord('a')] -= 1

    result = sum(map(abs, arr1))

    arr3.append(result)
    result = 0

for i in arr3:
    print(i)
