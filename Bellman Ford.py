graph=[[0,-4,999,999,999,-3],[999,0,999,-1,-2,999],[999,8,0,999,999,3],[6,999,999,0,999,4],[999,999,-3,999,999,2],[999,999,999,999,999,999]]
d=[999,999,999,999,999,999]
parent=[999,999,999,999,999,999]
e=[]
def edges():
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if (graph[i][j]!=0 and graph[i][j]!=999):
                print(f"{i}--->{j}")
                e.append((i,j))
edges()
def bellman(a,n):
    d[a]=0
    parent[a]=a
    j=1
    while(j<n):
        for i in range(len(e)):
            c=e[i][0]
            o=e[i][1]
            d[o]=min(d[o],d[c]+graph[c][o])
            parent[o]=c
        j+=1
bellman(0,6)
vertices=['a','b','c','d','e','t']
def print1(a):
    for i in range(1,len(vertices)):
        print(f"{vertices[a]}--->{vertices[i]}:{d[i]}")
print1(0)
