list=[6,7,8,9,10,11,12,13,14]
i=0
even=0
even_sum=0
even_count=0
odd=0
odd_sum=0
odd_count=0
while i<len(list):
	if list[i]%2==0:
		even_sum=even_sum+list[i]
		even_count=even_count+1
		avrage_even=even_sum/even_count
	else:
		odd_sum=odd_sum+list[i]
		odd_count=odd_count+1
		avrage_odd=even_sum/odd_count
	i=i+1
print(even_sum,"even sum")
print(even_count,"even count")
print(odd_sum,"odd sum")
print(odd_count,"odd count")
print(avrage_even,'even avrage')
print(avrage_odd,'odd avrage')