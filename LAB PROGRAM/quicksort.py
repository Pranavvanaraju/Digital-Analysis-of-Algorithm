def quicksort(a,first,last):
    if first<last:
        pivot=first
        i=first
        j=last
        while i<j:
            while a[i]<=a[pivot]:
                i+=1
            while a[j]>a[pivot]:
                j-=1
            if i<j:
                t=a[i]
                a[i]=a[j]
                a[j]=t
        t=a[pivot]
        a[pivot]=a[j]
        a[j]=t
        quicksort(a,first,j-1)
        quicksort(a,j+1,last)
    return a
a=[9,8,7,5,18,5,2,74]
print(quicksort(a,0,7))
