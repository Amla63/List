kitna_paisa_hai=[3000,600000,3249909090,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
count_dil=0
count_lakh=0
count_crore=0
while i<len(kitna_paisa_hai):
	if kitna_paisa_hai[i]<100000:
		count_dil=count_dil+1
	elif kitna_paisa_hai[i]>100000and kitna_paisa_hai[i]<1000000:
		count_lakh=count_lakh+1
	else:
		count_crore=count_crore+1
	i=i+1
print(count_dil,'dilwale')
print(count_lakh,'lakhpati')
print(count_crore,'crorepati')