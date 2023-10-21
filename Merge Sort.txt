import random
def mergesort(a,h,x):
    l=a[x:h+1]
    if (len(l)==2):
        if(l[0]>l[1]):
            l[0],l[1]=l[1],l[0]
        return l
    elif(len(l)==1):
        return l
    else:
        m=(h+x)//2
        b=mergesort(a,m,x)
        c=mergesort(a,h,m+1)
        l=merge(b,c)
        return l
def merge(b,c):
    i=0
    j=0
    d=[]
    while((i<len(b))and(j<len(c))):
        if(b[i]<c[j]):
            d.append(b[i])
            i+=1
        elif(b[i]==c[j]):
            d.append(b[i])
            i+=1
            j+=1
        else:
            d.append(c[j])
            j+=1
    while(j!=len(c)):
        d.append(c[j])
        j+=1
    while(i!=len(b)):
        d.append(b[i])
        i+=1
    return d
n=int(input("Enter the Number of elements"))
a=[]
for i in range(n):
    a.append(random.randint(1,100))
print(a)
a=mergesort(a,len(a),0)
print(a)
