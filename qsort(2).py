sr=0
pr=0
def part(a,l,h):
    global sr
    global pr
    p=a[l]
    b=l
    for i in range(1+l,h+1):
        if a[i]<=p:
            b+=1
            pr+=1
            a[i],a[b]=a[b],a[i]
    pr+=1
    a[l],a[b]=a[b],a[l]
    return b

def qsort(a,l,h):
    global sr
    global pr
    sr+=1
    if l<h:
        p=part(a,l,h)
        qsort(a,l,p-1)
        qsort(a,p+1,h)
    return a, sr, pr


c=list(map(int,input().split()))
print(qsort(c,0,len(c)-1))

