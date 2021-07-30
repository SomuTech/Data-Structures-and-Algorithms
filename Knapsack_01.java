import java.util.*;

class Knapsack_01
{
    static int algorithm(int W,int wt[],int p[],int n)
    {
        //sorting
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++)
            {
                if(p[i]<p[j]){
                    int temp=p[i]; p[i]=p[j]; p[j]=temp;
                    temp=wt[i]; wt[i]=wt[j]; wt[j]=temp;
                }
            }
        }

        int k[][]=new int[n+1][W+1];
        //initilize
        for(int i=0; i<n+1; i++){
            for(int j=0; j<W+1; j++)
                k[i][j]=0;
        }
        //calculation
        for(int r=0; r<n+1; r++)
        {
            for(int c=0; c<W+1; c++)
            {
                if(r==0 || c==0)
                    k[r][c]=0;
                else if(wt[r-1]<=W)
                    k[r][c]=Math.max(k[r-1][c],p[r-1]+k[r-1][W-wt[r-1]]);
                else 
                    k[r][c]=k[r-1][c];
            }
        }
        return k[n][W];
    }

    public static void main(String args[])
    {
        System.out.println("enter no.of profits:");
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int wt[]=new int[n],p[]=new int[n];
        for(int i=0;i<n; i++)
        {
            System.out.print("enter weight and value:");
            wt[i]=sc.nextInt();
            p[i]=sc.nextInt();
        }
        System.out.print("enter max weight of knapsack:");
        int W=sc.nextInt();
        System.out.println("Maximum profit:"+Knapsack_01.algorithm(W,wt,p,n));
    }
}