def unique(n):
    y = 0
    digits = count(n)
    x = n
    while(x>0):
        k = (x%10)
        y = (10*y) + k
        x = x//10
    z = y - n
    if(z<0):
        z = z* -1
    if(z == 9 or z == 198 or z == 3087 or z== 41976 or z==530865 ):
        return n
    else:
        continue

def count(n):
    c = 0
    while(n>0):
        c = c+1
        n = n//10
    return c

N = int(input())
arr = list(map(int,input().split()[:N]))
# arr = [int(i) for i in input().split()]
# for int(j) in arr:
#     print(unique(j))
print(arr)
sumu = 0
for i in arr:
    print(unique(i))
    sumu += unique(i)

print(sumu)
