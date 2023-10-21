#In this code vertex [1,2,3,4,6] are replaced with [0,1,2,3,4]
def prim(s,v,b):
    a=[s]#tree vertices
    e=[]#tree egde
    while(len(a)!=5):
        min=999
        for j in a:
            for i in v:
                if i in a:
                    continue
                if b[j][i]<=min:
                    min=b[j][i]
                    d=j
                    p=i
        e.append((d,p,b[d][p]))
        a.append(p)
    print(e)
b=[[0,4,999,8,999],[4,0,3,1,999],[999,3,0,7,8],[8,1,7,0,3],[999,999,8,3,0]]
v=[0,1,2,3,4]
prim(1,v,b)
