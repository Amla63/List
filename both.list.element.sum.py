list=[[9,8,7],[10,11,12],[9,17,19],[21,22,24]]
i=0
b=[]
while i<len(list):
	j=0
	max=0
	while j<len(list[i]):
		if list[i][j]>max:
			max=list[i][j]
		j=j+1
	b.append(max)
	i=i+1
print(b)
