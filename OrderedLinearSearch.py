# Ordered linear search

element=int(input("enter Roll Number:"))
def or_search(list,element):
    for i in range(len(list)):
        if(list[i]==element):
            return i
            break
        elif(list[i]>element):
            return -1
    return -1
result=or_search([10,11,12,13,17,18,19,20,21,22,23,24,25],element)
if(result==-1):
    print(element,"is not atttended for training")
else:
    print(element,"is atttended for training in",result+1,"place")
	
"""
output:
enter Roll Number:13
13 is atttended for training in 4 place
enter Roll Number:65
65 is not atttended for training
"""