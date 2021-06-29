list=[3,4,7,9,7,3,2,6,2]
i=0
a=[]
while i<len(list):
    j=0
    c=0
    b=[]
    while j<len(list):
        if list[i]==list[j]:
            c=c+1
        j=j+1
    if c>1:
        b.append(list[i])
        b.append(c)
        if b not in a:
            a.append(b)
    i=i+1
print(a)


