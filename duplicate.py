a=[1,1,3,5,3,8,9,5,6]
i=0
b=[]
while i<len(a):
	if a[i] not in b:
		b.append(a[i])
	i=i+1
print(b)