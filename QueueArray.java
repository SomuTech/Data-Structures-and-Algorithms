import java.util.*;
public class QueueArray 
{
    int item,size=5,front=-1,rear=-1,arr[]=new int[size];
    void enQueue(int item)
    {
        if(rear==size-1)
            System.out.println("queue is full!");
        else{
            if(rear==-1) front=0;
            rear+=1;
            arr[rear]=item;}
    }
    void deQueue()
    {
        if(rear==-1 || front>rear)
            System.out.println("queue is empty");
        else
        {
            if(front==size-1) rear=-1;
            System.out.println("item deleted:"+arr[front]);
            front+=1;
        }
    }
    void display()
    {
        if(rear==-1 || front==-1)
            System.out.println("empty");
        else{
            for(int i=front; i<=rear; i++)
            {
                System.out.print(arr[i]+" ");
            }
            System.out.println();
        }
    }
    public static void main(String args[])
    {
        QueueArray obj=new QueueArray();
        obj.enQueue(3);
        obj.enQueue(6);
        obj.display();
        obj.deQueue();
        obj.deQueue();
        obj.deQueue();
        obj.display();
    }
}
