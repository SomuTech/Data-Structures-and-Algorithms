//binary search implementation using recursion to search a roll number in an array
import java.util.*;
public class RecursiveBinarySearch
{
    static int binary(int rollNo[],int key,int n,int low,int high)
    {
        if(low<=high)
        {
            int mid=(low+high)/2;
            if(rollNo[mid]==key)
                return mid;
            else if(rollNo[mid]>key)
                return binary(rollNo,key,n,low,mid-1);
            else return binary(rollNo,key,n,mid+1,high);
        }
        return -1;
    }
    public static void main(String args[])
    {
        int rollNo[]={1,3,5,7,9},n=rollNo.length,key;
        Scanner sc=new Scanner(System.in);
        System.out.print("enter number to search:");
        key=sc.nextInt();
        int low=0,high=n-1;
        int result=binary(rollNo,key,n,low,high);
        if(result==-1)
            System.out.println("student not found");
        else
            System.out.println("student found in: "+(result+1));
    }
}
