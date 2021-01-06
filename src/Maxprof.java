import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Maxprof {
   public static void main(String[] args) {
       Solution s = new Solution();
       List<List<Integer>> t1 = s.largeGroupPositions("adbbbkkkhgggghgggddddd");
       for(int i=0;i<t1.size();i++){
           System.out.println(t1.get(i));
       }
   }
}

class Solution{
    public List<List<Integer>> largeGroupPositions(String s){
        List<List<Integer>> ret = new ArrayList<List<Integer>>();
        int n = s.length();
        int num = 1;
        for (int i = 0; i < n; i++) {
            if (i == n - 1 || s.charAt(i) != s.charAt(i + 1)) {
                if (num >= 3) {
                    ret.add(Arrays.asList(i - num + 1, i));
                }
                num = 1;
            } else {
                num++;
            }
        }
        return ret;
        
    }
}

