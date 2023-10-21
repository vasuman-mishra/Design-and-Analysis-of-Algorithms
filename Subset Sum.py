W=int(input("Enter the Sum needed:"))
n=4
a=[2,5,4,6]
m=[[0 for i in range(W+1)] for j in range(n+1)]
a.sort()
def subset(W, n):
    for i in range(1,n+1):
        for j in range(1,W+1):
            if a[i-1] <= j:
                m[i][j] = max(a[i-1] + m[i-1][j-a[i-1]],m[i-1][j])
            elif a[i-1] > j:
                m[i][j] = m[i-1][j]
o=[]
def pat():
    i=n
    b=W
    while(i!=0):
        if m[i][b]!=m[i-1][b]:
            o.append(a[i-1])
            b-=a[i-1]
        i-=1 
subset(W,4)
if m[n][W]==W:
    pat()
    print(o)
else:
    print("Sum Cannot be formed")
