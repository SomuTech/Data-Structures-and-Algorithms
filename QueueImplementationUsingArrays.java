import java.util.*;
class Steps{
	int item,size=5,rear=-1,front=-1,Arr[]=new int[size];
	void Enqueue(int item){
		if(rear==size-1){ System.out.println("Queue is full"); }
		else{
			if(rear==-1) front=0;
			rear++;
			Arr[rear]=item;
		}
	}
	void Dequeue(){
		if(rear==-1 || front>rear){
			System.out.println("Queue is empty");
			}
		else
		{	
			if(front==size-1) rear=-1;
			System.out.print("item deleted: "+Arr[front]);
			front+=1;	
			}
		}
	void display(){
		if(rear==-1 || front==-1) System.out.println("Queue is empty\n");
		else{
			System.out.print("Queue elements are: ");
			for(int i=front;i<=rear;i++){
				System.out.print(Arr[i]+" ");
			}
		}
	}

}
class QueueImplementationUsingArrays{
	public static void main(String args[]){	
		Steps obj=new Steps();
		boolean flag=true;
		while(flag){
			Scanner sc=new Scanner(System.in);
			System.out.println("enter 1.Enqueue\t2.Dequeue\t3.display\t4.exit");
			System.out.print("enter option:");
			int op=sc.nextInt();
			switch(op)
			{
				case 1:
					System.out.print("enter item:");
					obj.item=sc.nextInt();
					obj.Enqueue(obj.item); break;
				case 2:
					obj.Dequeue(); break;
				case 3:
					System.out.print("items in Queue:");
					obj.display(); break;
				case 4:
					flag=false; break;
				default:System.out.println("\ntry again"); 
			}
}}}
