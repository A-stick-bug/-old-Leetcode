package leetcode;
import java.util.Arrays;

public class Q_1051_check_sorted {
    public int heightChecker(int[] heights) {
        int[] old_arr = heights.clone();
        Arrays.sort(heights);
        int misplaced = 0;

        for (int i = 0;i < heights.length;i++){
            if (heights[i] != old_arr[i])
                misplaced ++;
        }
        return misplaced;
    }
}
