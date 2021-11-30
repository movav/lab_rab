def part(a,l,h):
    p=a[l]
    b=l
    for i in range(1+l,h+1):
        if a[i]<=p:
            b+=1
            a[i],a[b]=a[b],a[i]
    a[l],a[b]=a[b],a[l]
    return b

def qsort(a,l,h):
    if l<h:
        p=part(a,l,h)
        qsort(a,l,p-1)
        qsort(a,p+1,h)
    return a


a=[1,3,5,7,2,8,6,4,10]
print(qsort(a,0,len(a)-1))