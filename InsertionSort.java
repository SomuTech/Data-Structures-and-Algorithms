public class InsertionSort
{
    public static void main(String args[])
    {
        int arr[]={2,1,3,5,3,8},v,j;
        int n=arr.length;
        for(int i=1; i<=n-1; i++)
        {
            v=arr[i];
            j=i;
            while(arr[j - 1] > v && j >= 1)
            {
                arr[j]=arr[j-1];
                j=j-1;
            }
            arr[j]=v;
        }
        System.out.print("sorted array:");
        for(int item:arr) System.out.print(item+" ");
    }
}
