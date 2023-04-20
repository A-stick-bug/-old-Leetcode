package leetcode;

public class Q_1295_even_digits {
    public static int findNumbers(int[] nums) {
        int count = 0;
        for (int num : nums) {
            boolean even_digit = false;
            while (num >= 10) {
                num/=10;
                even_digit = !even_digit;
            }
            if (even_digit)
                count ++;
        }
        return count;
    }
    public static void main(String[] args){
        System.out.println(findNumbers(new int[]{100000}));
    }
}
