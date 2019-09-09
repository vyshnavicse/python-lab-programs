fname=input("enter the filename")
fn=open(fname,"r")
d=dict()
for line in fn:
    for ch in line:
        if ch in d:
            d[ch]=d[ch]+1
        else:
            d[ch]=1
print("frequency of characters is")
print(d)
fn.close()

        
