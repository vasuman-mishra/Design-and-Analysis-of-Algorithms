#countinginversion
def countinv(a,l,h):
    c=0
    if(l<h):
        m=(l+h)//2
        c+=countinv(a,l,m)
        c+=countinv(a,m+1,h)
        c+=merge(a,l,m+1,h)
    return c
def merge(a,l,m,h):
    i=l
    j=m
    co=0
    c=[0 for x in range(h-l+1)]
    k=0
    while(i<m and j<=h):
        if a[i]<=a[j]:
            c[k]=a[i]
            i+=1
            k+=1
        else:
            c[k]=a[j]
            co+=(m-i)
            j+=1
            k+=1
    while(i<m):
        c[k]=a[i]
        i+=1
        k+=1
    while(j<=h):
        c[k]=a[j]
        j+=1
    k = 0
    for i in range(l, h + 1):
        a[i] = c[k]
        k += 1
    return co
a=[8,1,4,5,6,14,7,3]
print(f"The list is:{a}")
c=countinv(a,0,len(a)-1)
print(f"The Number of Inversion are:{c}")
