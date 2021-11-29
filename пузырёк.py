def bubl(a):
    sr=0
    pr=0
    for i in range(len(a)):
        for j in range(len(a)-1,0,-1):
            sr+=1
            if a[j]<a[j-1]:
                pr+=1
                a[j],a[j-1]=a[j-1],a[j]
    print('сравнение=',sr)
    print('перестановки=',pr)
    return a
