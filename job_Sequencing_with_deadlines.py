def jobSequencing(job,profit,deadline, slot):
    n=len(job)
    #sorting:
    for i in range(n):
        for j in range(n-1-i):
            if profit[j]<profit[j+1]:
                profit[j],profit[j+1]=profit[j+1],profit[j]
                job[j],job[j+1]=job[j+1],job[j];
                deadline[j],deadline[j+1]=deadline[j+1],deadline[j]

    result=[False]*slot
    sequence=['-1']*slot
    max_profit=0                         
    #sequencing
    for i in range(n):
        for j in range(min(slot-1,deadline[i]-1),-1,-1):
            if result[j] is False:
                result[j]=True
                max_profit+=profit[i]
                sequence[j]=job[i]
                break

    #output:
    print("job sequence with maxmum profit: ",sequence)
    print("\nmaximum profit: ",max_profit)
                
#input:
profit=[100,19,27,25,15]
job=[1,2,3,4,5]
deadline=[2,1,2,1,3]
jobSequencing(job,profit,deadline,3)

