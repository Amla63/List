list=[3,5,6,7,8,9,3,22,23]
i=0
max=0
sec_max=0
third_max=0
while i<len(list):
    if list[i]>max:
        sec_max=max
        max=list[i]
    elif sec_max<list[i] and max>list[i]:
        third_max=sec_max
        sec_max=list[i]
    elif third_max<list[i] and sec_max<list[i] and max>list[i]:
        third_max=list[i]
    i=i+1
print(third_max)
