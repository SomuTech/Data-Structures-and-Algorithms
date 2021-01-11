#Non recursive

num=int(input("enter the number:"))
def binary(l,h,list,num):
    for l in range(h+1):
        mid=(l+h)//2
        if(list[mid]==num):
            return mid
        elif list[mid]>num:
            h=mid-1
        else:
                l=mid+1
    return -1
list=[10,11,12,13,17,18,19,20,21,22,23,24,25]
result=binary(0,len(list)-1,list,num)
if result==-1:
    print(num,"is not atttended for training")
else:
    print(num,"is atttended for training in",result+1,"place")

"""output:
enter the number:20
20 is atttended for training in 8 place
enter the number:39
39 is not atttended for training
"""