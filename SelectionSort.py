# 1c.Selection sort:

def sel_sort(list):
    for i in range(len(list)):
        min_num=i
        for j in range(i+1,len(list)):
            if(list[min_num]>list[j]):
                min_num=j
        list[min_num],list[i]=list[i],list[min_num]
    print("List after selection sort",list)
sel_sort([21,45,-58,-789,54,32,1,855])

#output:
#List after selection sort [-789, -58, 1, 21, 32, 45, 54, 855]