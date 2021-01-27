//binary search implementation to search whether a student is present or not
import java.util.*;
public class BinarySearch 
{
    static int binary(int rollNo[],int key,int n)
    {
        int low=0,high=n-1;
        while(low<=high)
        {
            int mid=(low+high)/2;
            if(rollNo[mid]==key)
                return mid;
            else if(rollNo[mid]>key)
                high=mid-1;
            else low=mid+1;
        }
        return -1;
    }
    public static void main(String args[])
    {
        int rollNo[]={1,3,5,7,9},n=rollNo.length,key;
        Scanner sc=new Scanner(System.in);
        System.out.print("enter number to search:");
        key=sc.nextInt();
        int result=binary(rollNo,key,n);
        if(result==-1)
            System.out.println("student not found");
        else
            System.out.println("student found in: "+(result+1));
    }
}
