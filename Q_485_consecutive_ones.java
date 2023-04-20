package leetcode;

public class Q_485_consecutive_ones {
    public static int findMaxConsecutiveOnes(int[] nums){
        int max = 0;
        int current = 0;
        for (int num : nums) {
            if (num == 1)
                current++;
            else {
                max = Math.max(current, max);
                current = 0;
            }
        }
        max = Math.max(current, max);
        return max;
    }
    public static void main(String[] args){
        int[] numbers = {1,1,0,1,1,1};
        System.out.println(findMaxConsecutiveOnes(numbers));
    }
}
