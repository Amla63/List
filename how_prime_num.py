num=int(input("enter the num"))
i=1
while i<=num:
    j=1
    c=0
    while j<=num:
        if i%j==0:
            c=c+1
        j=j+1
    i=i+1
print(c)
