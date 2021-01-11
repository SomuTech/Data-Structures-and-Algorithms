#Unordered linear search

element=int(input("enter Roll Number:"))
def un_search(list,element):
    for i in range(len(list)):
        if(list[i]==element):
            print(element,"is atttended for training in ",i+1,"place")
            break
    else:
       print(element,"is not atttended for training") 
result=un_search([10,12,11,25,23,20,18,19,13,17,21,22,24],element)

"""
output:
enter Roll Number:12
12 is atttended for training in  2 place
enter Roll Number:35
35 is not atttended for training
"""