//unordered linear search implementation 
import java.util.*;
public class OrderedLinearSearch
{
    public static void main(String args[])
    {
        int rollNo[]={1,2,5,6,7},n=rollNo.length,element;
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
            else if (i==n-1 || rollNo[i]>element){
                System.out.println("student not attended for training");
                break;}
        }
    }
}
