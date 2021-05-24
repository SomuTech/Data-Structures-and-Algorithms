class GreedyMethod
{
    static void jobSequence(int job[],int profit[],int deadline[],int slot)
    {
        int n=job.length;
        //sorting
        for(int i=0; i<n; i++)
            for(int j=i; j<n-1-i; j++){
                    if(profit[j]<profit[j+1]){
                        int temp=profit[j]; profit[j]=profit[j+1];profit[j+1]=temp;
                        temp=job[j]; job[j]=job[j+1]; job[j+1]=temp;
                        temp=deadline[j]; deadline[j]=deadline[j+1]; deadline[j+1]=temp;
                    }
                }
        boolean result[]=new boolean[slot];
        int sequence[]=new int[slot];
        for(int i=0;i<slot; i++){
                result[i]=false;
                sequence[i]=-1;
        }   
        int max_profit=0;
        //sequence
        for(int i=0;i<n;i++)
            for (int j= Math.min(slot-1,deadline[i]-1);j>=0;j--){
                if(result[j]==false){
                    result[j]=true;
                    max_profit+=profit[i];
                    sequence[j]=job[i];
                    break;
                }
            }
        System.out.print("maximum profit sequence:");
        for(int i:sequence)
            System.out.print(i+" ");
        System.out.println("\nmaximum profit:"+max_profit);
    }

    public static void main(String args[])
    {
        int job[]={1,2,3,4},profit[] ={100,10,15,27},deadline[]={2,1,2,1};
        jobSequence(job, profit, deadline,4);
    }
}

/*OUTPUT:
maximum profit sequence:4 1 -1 -1
maximum profit:127*/