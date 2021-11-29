def vbr(a):
    sr=0
    pr=0
    for i in range(len(a)):
        k=i
        x=a[i]
        for j in range(i+1,len(a)):
            sr+=1
            if a[j]<x:
                pr+=1
                k=j
                x=a[j]
        a[k]=a[i]
        a[i]=x
    print('сравнения=',sr)
    print('перестановки=',pr)
    return a
