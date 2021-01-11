# 1a.Bubble sort program:

list=[21,45,-58,-789,54,32,1,855]
for i in range(len(list)-1):
    for j in range(0,len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
print("list after bubble sorting:",list)

#output:
#list after bubble sorting: [-789, -58, 1, 21, 32, 45, 54, 855]