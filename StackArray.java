import java.util.*;   
public class StackArray 
{
    int item,size=5,top=0,arr[]=new int[size];
    void push(int item)
    {
        if(top>=size) 
            System.out.println("stack is full!");
        else
        {
            arr[top]=item;
            top=top+1;
        }
    }
    void peek()
    {
        if(top<1)
            System.out.println("stack is empty!");
        else
        {
            System.out.println("peeked item:"+arr[top-1]);
        }
    }
    void pop()
    {
        if(top<1)
        System.out.println("stack is empty!");
        else
        {
            System.out.println("poped item:"+arr[top-1]);
            top=top-1;
        }
    }
    void display()
    {
        if(top<1)
            System.out.println("stack is empty");
        else
        {
            for(int i=top-1; i>=0; i--)
            {
                System.out.print(arr[i]+" ");
            }
            System.out.println();
        }
    }
    public static void main(String args[])
    {
        StackArray obj=new StackArray();
        obj.push(7);
        obj.push(4);
        obj.push(3);
        obj.pop();
        obj.peek();
        obj.pop();
        obj.display();
        obj.pop();
        obj.display();
    }
}
