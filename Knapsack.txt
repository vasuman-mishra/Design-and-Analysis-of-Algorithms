W=7
n=4
a=[[3,10],[5,4],[6,9],[2,11]]

m=[[0 for i in range(W+1)] for j in range(n+1)]
w=[]
v=[]
for i in a:
    w.append(i[0])
w.sort()
for i in w:
    for j in a:
        if i==j[0]:
            v.append(j[1])
def knapsack(w, v, W, n):
    for i in range(1,n+1):
        for j in range(1,W+1):
            if w[i-1] <= j:
                m[i][j] = max(v[i-1] + m[i-1][j-w[i-1]],m[i-1][j])
            elif w[i-1] > j:
                m[i][j] = m[i-1][j]
o=[]
def pat():
    a=n
    b=W
    while(a!=0):
        if m[a][b]!=m[a-1][b]:
            o.append(a)
            b-=w[a-1]
        a-=1 
knapsack(w,v,W,4)
print(f"The maximum value is:{m[n][W]}")
pat()
for i in o:
    print(f"wieght:{w[i-1]}-->value:{v[i-1]}")
