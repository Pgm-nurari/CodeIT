import java.util.*;

class Items{
    int itemCode;
    String itemName;
    int itemQuantity;
    float itemPrice;

    Scanner itemScanner = new Scanner(System.in);

    void storeData(){
        System.out.println("Enter the item code: ");
        itemCode = itemScanner.nextInt();
        System.out.println("Enter the name of the item: ");
        itemName = itemScanner.next();
        System.out.println("Enter quantity: ");
        itemQuantity = itemScanner.nextInt();
        System.out.println("Enter the price of the item: ");
        itemPrice = itemScanner.nextFloat();
    }

    void displayItemData(){
        String result = String.format("Item Code: %d\nItem Name: %s\nItem Quantity: %d\nItem Price: %f.3", itemCode, itemName, itemQuantity, itemPrice);
        System.out.println(result);
    }
}
public class Main {
    
    public static void main(String[] args) {

        Items[] itemList = new Items[3];

        System.out.println("Enter the data for 3 items of your choice: ");
        for (int i = 0; i < 1; i++){
            itemList[i] = new Items();
            itemList[i].storeData();
        }

        System.out.print("\033[H\033[2J");
        System.out.flush();

        System.out.println("Displaying the 3 items:");
        for (int i = 0; i < 1; i++){
            System.out.println("Item" + (i+1) + ":\n------------------------");
            itemList[i].displayItemData();
        }
    }    
}
