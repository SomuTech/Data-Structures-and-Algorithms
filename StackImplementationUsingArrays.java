import java.util.*;
class Steps{
	int item,size=5,Top=0,Arr[]=new int[size];
	void push(int item){
		if(Top>=size){ System.out.println("Stack is full"); }
		else {
			Arr[Top]=item;
			Top=Top+1;}
	}
	void pop(){
		if(Top<1){ System.out.println("Stack is Empty"); }
		else{
			item =Arr[Top-1];
			Top=Top-1; 
			System.out.println("poped item:"+item);}
	}
	void peek(){
		if(Top<1){ System.out.println("Stack is Empty"); }
		else
			{System.out.println("peeked item:"+Arr[Top-1]);}
	}
	static int palindrome(int Arr[],int b,int e){
		if(b>=e){ return 1; }
		if(Arr[b]==Arr[e]){ return palindrome(Arr,b+1,e-1); }
		else
			{return 0;}
	}
	void display(){
		for(int i=Top-1; i>=0; i--) { System.out.print(Arr[i]+"  "); }
		System.out.print("\n");}
}
public class StackImplementationUsingArrays
{
	public static void main(String args[]){
		Steps obj=new Steps();
		boolean flag=true;
		while(flag){
			Scanner sc=new Scanner(System.in);
			System.out.println("1.push\t2.pop\t3.peek\t4.display\t5.palindrome\t6.exit");
			System.out.print("enter option:");
			int op=sc.nextInt();
			switch(op)
			{
				case 1:
					System.out.print("enter item:");
					obj.item=sc.nextInt();
					obj.push(obj.item); break;
				case 2:
					obj.pop(); break;
				case 3:
					obj.peek(); break;
				case 4:
					System.out.print("items in stack:");
					obj.display(); break;
				case 5:
					if(obj.palindrome(obj.Arr,0,obj.size-1)==1){
						System.out.println("palindrome"); }
					else
						System.out.println("not a palindrome"); break;
				case 6:
					flag=false; break;
				default:System.out.println("\ntry again"); 
			}
}}}

