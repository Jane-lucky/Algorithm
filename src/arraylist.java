import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class arraylist {
    public static void main(String[] args) {
        String[] myarray = {"Apple","Banana","Orange"};
        List<String> myList = new ArrayList<String>();
        for(String str:myarray){
            myList.add(str);
            myList.add(str);
        }
        System.out.println(myList.size());
    }
    
}
