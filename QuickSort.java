import java.util.*;
class QuickSort
{
	void quick(int arr[],int low,int high)
	{
		if(low <high)
		{
			int pi=partition(arr,low,high);	
			quick(arr,pi+1,high);
			quick(arr,low,pi-1);	
		}
	}
	int partition(int arr[],int low,int high)
	{
		int p=arr[high],i=low-1;
		for(int j=low;j<=high-1;j++)
		{
			if(arr[j]<p)
			{
				i++;
				int temp=arr[j]; arr[j]=arr[i]; arr[i]=temp;
			}
		}
		int temp=arr[i+1]; arr[i+1]=arr[high]; arr[high]=temp;
		return (i+1);
	}
	public static void main(String args[])
	{
		int arr[]={45,78,69,-2,65,74};
		QuickSort obj1=new QuickSort();
		obj1.quick(arr,0,arr.length-1);
		for(int i:arr)
			System.out.print(i+" ");
	}
}