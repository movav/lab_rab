def shell(a):
    sr=0
    pr=0
    n=len(a)
    p=n//2
    while p>0:
        for i in range(p):
            for j in range(i+p,len(a),p):
                x=a[j]
                po=j
                sr+=1
                while po>=p and a[po-p]>x:
                    pr+=1
                    a[po]=a[po-p]
                    po=po-p
                a[po]=x
        p=p//2
    print('сравнения=',sr)
    print('перестановки=',pr)
    return a
