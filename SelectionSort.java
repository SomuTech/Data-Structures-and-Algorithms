public class SelectionSort
{
    public static void main(String args[])
    {
        int arr[]={2,3,1,4,7,5};
        int i,j,min,n=arr.length;
        for(i=0; i<n-1;i++)
        {
            min=i;
            for(j=i+1; j<n; j++)
            {
                if(arr[j]<arr[min])
                {
                    min=j;
                }
            }
            int temp=arr[min];
            arr[min]=arr[i];
            arr[i]=temp;
        }
        System.out.print("sorted array:");
        for(int item:arr)
            System.out.print(item+" ");
    }
}
