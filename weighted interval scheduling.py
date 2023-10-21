#weightedintervalscheduling
p=[]
m=[]
for i in range(6):
    p.append(0)
    m.append(0)
def sort1(d):
    b=[]
    for i in d:
        b.append(i[1])
    b.sort()
    c=[]
    for i in b:
        for j in d:
            if i==j[1]:
                c.append(j)
    return c
def prev(p,d):
    for i in range(len(d)):
        if (i==6):
            break
        for j in range(i):
            if d[i][0]>=d[j][1]:
                p[i]=j
    return p
def opt(p,d,m):
    for i in range(len(m)):
        if (d[i][2]+m[p[i]])>m[i-1]:
            m[i]=d[i][2]+m[p[i]]
        else:
            m[i]=m[i-1]
    return m
    return p
def path1(p,m):
    for i in range(-1,-len(m)-1,-1):
        if m[i]!=m[i-1]:
            j=len(m)+i
            print(j+1)
            a=999
            while(a!=0):
                a=p[j]
                print(a+1)
                a=p[a]
                print(a+1)
            break
d=[]
n=int(input("Enter Number of jobs:"))
for i in range(n):
    a=[]
    a.append(int(input("Enter the Start time:")))
    a.append(int(input("Enter the Finish time:")))
    a.append(int(input("Enter the value:")))
    d.append(a)
d=sort1(d)
p=prev(p,d)
m=opt(p,d,m)
print(m[5])
path1(p,m)
