#DFS
visited=[]
def dfs(o):
    visited[int(o)]=1
    print(o)
    a=d[o]
    for i in range(len(d[o])):
        for i in a:
            if visited[int(i)]==0:
                return dfs(i)
def create(n):
    for i in range(n):
        visited.append(0)
d={}
def make(l):
    if (d=={}):
        d[l[0]]=[]
        d[l[1]]=[]
        d[l[0]].append(l[1])
        d[l[1]].append(l[0])
    else:
        if ((l[0] in d.keys())and(l[1] in d.keys())):
            d[l[0]].append(l[1])
            d[l[1]].append(l[0])
        elif (l[0] in d.keys()):
            d[l[0]].append(l[1])
            d[l[1]]=[]
            d[l[1]].append(l[0])
        else:
            d[l[1]].append(l[0])
            d[l[0]]=[]
            d[l[0]].append(l[1])
n=int(input("enter the number of edges:"))
for i in range(n):
    l=[]
    l=input("enter the edge").split()
    make(l)
print(d)
create(n)
dfs('0')