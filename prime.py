x=int(input("enter a number"))
c=2
for i in range(2,int(x/2+1)):
    if x%i==0:
        c=c+1
        break
if c==2:
    print(x,"is a prime number")
else:
    print(x,"is not a prime number")


