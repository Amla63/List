list=[3,4,6,8,9,0,3,5,45,6,7,36]
i=0
max=0
sec_max=0
while i<len(list):
    if list[i]>max:
        sec_max=max
        max=list[i]
    elif sec_max<list[i] and max>list[i]:
        sec_max=list[i]
    i=i+1
print(sec_max)

