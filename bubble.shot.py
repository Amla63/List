list=[1,5,4,2,3]
i=0
while i<len(list):
	j=0
	while j<(len(list)-1):
		if list[j]>list[j+1]:
			list[j],list[j+1]=list[j+1],list[j]
		j=j+1
	i=i+1
print(list)
