d1 = {'a': ['v','w','x'], 'b': ['w','v','x'], 'c': ['v','w','x']}
d2 = {'v': ['a','b','c'], 'w': ['b','c','a'], 'x': ['c','a','b']}
t = []
o = []
p = []
for i in d1.keys():
    while i not in t:
        for j in range(3):
            if d1[i][j] not in o:
                d = [i, d1[i][j]]
                p.append(d)
                t.append(i)
                o.append(d1[i][j])
                break
            else:
                y = 0
                for u in p:
                    if u[1] == d1[i][j]:
                        break
                    y += 1
                if d2[d1[i][j]].index(i) < d2[d1[i][j]].index(p[y][0]):
                    d = [i, d1[i][j]]
                    p.append(d)
                    t.append(i)
                    t.remove(p[y][0])
                    i = p[y][0]
                    del p[y]
                else:
                    pass
print(p)
