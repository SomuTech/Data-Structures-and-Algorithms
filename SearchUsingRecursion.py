# Recursive 

num=int(input("enter the number:"))
def binary(l,h,list,num):
    if l<=h:
        mid=(l+h)//2
        if list[mid]==num:
            return mid
        elif list[mid]>num:
            return binary(l,mid-1,list,num)
        else:
            return binary(mid+1,h,list,num)
    
    else:
        return -1
list=[10,11,12,13,17,18,19,20,21,22,23,24,25]
result=binary(0,len(list)-1,list,num)
if result==-1:
    print(num,"is not atttended for training")
else:
    print(num,"is atttended for training in ",result+1,"place")

"""
output:
enter the number:18
18 is atttended for training in  6 place
enter the number:66
66 is not atttended for training
"""