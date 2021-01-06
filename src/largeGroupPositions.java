import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class largeGroupPositions {
   public static void main(String[] args) {
       Solution s = new Solution();
       List<List<Integer>> t1 = s.largeGroup("adbbbkkkhgggghgggddddd");
       for(int i=0;i<t1.size();i++){
           System.out.println(t1.get(i));
       }
   }
}

class Solution{
    /*
    在一个由小写字母构成的字符串 s 中，包含由一些连续的相同字符所构成的分组。

例如，在字符串 s = "abbxxxxzyy" 中，就含有 "a", "bb", "xxxx", "z" 和 "yy" 这样的一些分组。

分组可以用区间 [start, end] 表示，其中 start 和 end 分别表示该分组的起始和终止位置的下标。上例中的 "xxxx" 分组用区间表示为 [3,6] 。

我们称所有包含大于或等于三个连续字符的分组为 较大分组 。
    */
    public List<List<Integer>> largeGroup(String s){
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

