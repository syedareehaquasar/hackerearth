a = input()
n = len(a)-len(a)

for i in range(len(a)):
    if a[i] in ['G', 'C', 'T', 'A']:
        n += len(a)/len(a)

n = int(n)
a = list(a)
if n is len(a):
    for i in range(len(a)):
        if a[i] is 'G':
            a[i] = 'C'
        elif a[i] is 'C':
            a[i] = 'G'
        elif a[i] is 'T':
            a[i] = 'A'
        elif a[i] is 'A':
            a[i] = 'U'

    a = "".join(map(str, a))
    print(a)
else:
    print("Invalid Input")
