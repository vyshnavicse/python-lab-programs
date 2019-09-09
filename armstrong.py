n=int(input("enter a number"))
sum=0
m=n
while n>0:
    r=n%10
    sum=sum+(r*r*r)
    n=n//10
if sum==m:
    print(sum,"is an armstrong number")
else:
    print(sum,"is not an armstrong number")
