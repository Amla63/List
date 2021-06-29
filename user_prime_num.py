num=int(input("enter the num"))
i=1
count=0
while i<=num:
    if num%i==0:
        count+=1
    i=i+1
if count==2:
    print(num,"is prime num")
else:
    print(num,"is not prime num")