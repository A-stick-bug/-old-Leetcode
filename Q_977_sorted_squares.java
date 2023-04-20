package leetcode;
import java.util.Arrays;

public class Q_977_sorted_squares {
    public static int[] sortedSquares(int[] nums) {
        for (int i = 0;i< nums.length;i++){
            nums[i] = nums[i]*nums[i];
        }
        Arrays.sort(nums);
        return nums;
    }
}
