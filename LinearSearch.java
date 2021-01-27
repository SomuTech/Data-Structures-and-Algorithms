//Linear search implementation to search a student in an array
import java.util.*;
public class LinearSearch
{
    public static void main(String args[])
    {
        int rollNo[]={1,2,5,3,4,7},n=rollNo.length,element;
        Scanner sc=new Scanner(System.in);
        System.out.print("enter roll number to search:");
        element=sc.nextInt();
        for(int i=0; i<n; i++)
        {
            if(rollNo[i]==element)
            {
                System.out.println("student attended for Training");
                break;
            }
            else if (i==n-1)
                System.out.println("student not attende for training");

        }
    }
}