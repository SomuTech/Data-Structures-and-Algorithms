class MergeSort
{
	void divide(int arr[],int l,int h)
	{
		if(l<h){
			int m=(l+h)/2;
			divide(arr,l,m);
			divide(arr,m+1,h);
			merge(arr,l,m,h);
		}
	}
	void merge(int arr[],int l,int m,int h)
	{
		int n1=m-l+1,n2=h-m;
		int la[]=new int[n1],ra[]=new int[n2];
		for(int i=0;i<n1;++i)
			la[i]=arr[l+i];
		for(int j=0;j<n2;++j)
			ra[j]=arr[m+1+j];
		int i=0,j=0,k=l;
		while(i<n1&&j<n2){
			if(la[i]<=ra[j]){
				arr[k]=la[i];
				i++;}
			else{
				arr[k]=ra[j];
				j++;
			}
			k++;
		}
		while(i<n1){
			arr[k]=la[i];
			i++;
			k++;
		}
		while(j<n2){
			arr[k]=ra[j];
			j++;
			k++;
		}
	}
	public static void main(String args[])
	{
		int arr[]={45,78,69,-2,65,74};
		MergeSort obj=new MergeSort();
		obj.divide(arr,0,arr.length-1);
		for(int i:arr)
			System.out.print(i+" ");
	}
}