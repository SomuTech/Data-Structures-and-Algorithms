# 1b.Insertion sort program

def ins_sort(n):
    for i in range(1,len(n)-1):
        v=n[i]
        j=i
        while(n[j-1]>v and j>=1):
            n[j]=n[j-1]
            j=j-1
        n[j]=v
    print("List after Insertion sort",n)
ins_sort([7,6,5,8,3,1,45,12,19])

#output:
#List after Insertion sort [1, 3, 5, 6, 7, 8, 12, 45, 19]