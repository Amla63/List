a=[3,4,6,19,12]
i=0
c=0
while i<len(a):
    if a[i]>3 and a[i]<10:
        print(a[i])
        c=c+1
    i=i+1
print(c)