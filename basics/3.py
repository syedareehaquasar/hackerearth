"""

You have been given a String S. You need to find and print whether this string is a palindrome or not.
If yes, print "YES" (without quotes), else print "NO" (without quotes).

Input Format
The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

Output Format
Print the required answer on a single line.

Constraints

Note
String S consists of lowercase English Alphabets only.

"""

str1 = input()
n = len(str1)
count = 0
if n % 2 is 0:
    n /= 2
    n = int(n)

else:
    n /= 2
    n = int(n)
j = len(str1) - 1
i = 0
while j > i:
    if str1[i] is str1[j]:
        count += 1
    j -= 1
    i += 1

if count is n:
    print("YES")
else:
    print("NO")
