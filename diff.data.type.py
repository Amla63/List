list=["amla","2","3","jyoti","2.5"]
i=0
a=[]
n = 0
while n < len(list):
    try:
        list[n] = int(list[n])
        a.append(type(list[n]))
    except:
        try:
            list[n] = float(list[n])
            a.append(type(list[n])) 
        except:
            a.append(type(list[n]))
    n += 1
print(a)






