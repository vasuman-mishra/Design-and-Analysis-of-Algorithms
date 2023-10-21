#insertionsort
def insertionSort(l):
    for i in range(1,len(l)):
        key = l[i]
        j=i-1
        while (j >= 0 and l[j] > key):
            l[j+1],l[j]=l[j],l[j+1]
            j=j-1
    return l
a=[2,1,6,5,4,3]
a=insertionSort(a)
print(a)