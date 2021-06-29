a=[2,4,5,7,8,4,9,1]
i=0
largest=0
while i<len(a):
	if a[i]>largest:
		largest=a[i]
	i=i+1
print(largest)