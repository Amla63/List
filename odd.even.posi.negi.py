a=[1,3,5,7,-5,-8,-9,-3,0,5,7,0,-8,4,0,3,-1,-10,12,0]
i=0
even=0
odd=0
zero=0
positive=0
negitive=0
while i<len(a):
	if a[i]%2==0:
		even=even+1
	if a[i]%2!=0:
		odd=odd+1
	if a[i]==0:
		zero=zero+1
	if a[i]>0:
		positive=positive+1
	if a[i]<0:
		negitive=negitive+1
	i=i+1
print(even)
print(odd)
print(zero)
print(positive)
print(negitive)