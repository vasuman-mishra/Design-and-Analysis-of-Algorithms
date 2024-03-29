#quicksort
def partition(a,l,h):
    i=l+1
    j=h
    pivot=a[l]
    while(i<=j):
        while(i<=j and a[i]<=pivot):
            i+=1
        while(i<=j and a[j]>=pivot):
            j-=1
        if(i<j):
            a[i],a[j]=a[j],a[i]
    a[j],a[l]=a[l],a[j]
    return j
def quicksort(a,l,h):
    if(l<h):
        p=partition(a,l,h)
        quicksort(a,l,p-1)
        quicksort(a,p+1,h)
a=[1,2,3,4]
print(a)
quicksort(a,0,3)
print(a)
