n=4
b=[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
def safe(row,col):
    for i in range(col):
        if b[row][i]==1:
            return False
    i=row
    j=col
    while(i>-1 and j>-1):
        if b[i][j]==1:
            return False
        i-=1
        j-=1
    i=row
    j=col
    while(i<n and j>-1):
        if b[i][j]==1:
            return False
        i+=1
        j-=1
    return True
def nq(col):
    if col>=n:
        return True
    for i in range(n):
        if safe(i,col):
            b[i][col]=1
            if nq(col+1)==True:
                return True
            b[i][col]=0
    return False
def prints():
    for i in range(n):
        for j in range(n):
            if b[i][j]==0:
                print("_",end=" ")
            else:
                print("Q",end=" ")
        print("\n")
nq(0)
prints()
