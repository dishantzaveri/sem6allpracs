import java.util.*;
public class hiring
{
 
public static void main (String[]args)
  {
    int order[] = new int[10];
     
int k = 0, hc = 20, fc = 10, threshold = 3, cost = 0;
      ArrayList < Integer > list = new ArrayList < Integer > (10);
     
for (int i = 1; i <= 10; i++)
      {
    list.add (i);
     
}
Random rand = new Random ();
    while (list.size () > 0)
      {
   
int index = rand.nextInt (list.size ());
    System.out.println ("Selected: " + list.get (index));
    order[k++] = list.remove (index);
   
}
 
for (int j = 0; j < 10; j++)
      {
    cost++;
    if (order[j] > threshold)
      {
       
cost += hc + fc;
        threshold = order[j];
     
}
   
System.out.println ("Cost after " + (j + 1) + "th candidate = " +
                 cost);
     
}
 
}


}