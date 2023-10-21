graph=[[999,10,999,999,5],[10,999,1,6,999],[999,1,999,2,7],[999,6,2,999,3],[5,999,7,3,999]]
p=[0,1,2,3,4]
def parent(a):
    while p[a]!=a:
        a=p[a]
    return a
def rank(a,b):
    i=parent(a)
    j=parent(b)
    p[i]=j 
def kruskal():
    e=0
    cost=0
    while e<4:
        m=999
        c=0
        d=0
        for i in range(len(graph)):
            for j in range (len(graph)):
                if parent(i)!=parent(j) and graph[i][j]<m:
                    m=graph[i][j]
                    c=i
                    d=j
        rank(c,d)
        print(f"{c+1}-->{d+1} with weight:{m}")
        cost+=m
        e+=1
    print(f"Mininmum Cost:{cost}")
kruskal()
