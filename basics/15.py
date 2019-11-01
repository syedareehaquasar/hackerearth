n = int(input())
x = int(input())
y = []
for i in range(n):
    y.append(int(input()))

for i in range(n):
    if y[i] >= x:
        print("YES")
    else:
        print("NO")
