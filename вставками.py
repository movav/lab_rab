def vst(a):
    sr=0
    pr=0
    for i in range(1,len(a)):
        k=a[i]
        n=i-1
        sr+=1
        while n>=0 and k<a[n]:
            pr+=1
            a[n+1]=a[n]
            n-=1
        a[n+1]=k
    print('сравнения=',sr)
    print('перестановки=',pr)

