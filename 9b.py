def dup(a):
    s=set()
    d=set()
    for i in a:
        if i in s:
            d.add(i)
        else:
            s.add(i)
    print(d)
dup([1,1,2,2,3,3,4,5,5,8])     
