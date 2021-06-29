name=['m','o','m']
i=-1
j=[]
while i>=(-len(name)):
	j.append(name[i])
	i=i-1
if j==name:
	print('its palindrome')
else:
	print('not palindrome')