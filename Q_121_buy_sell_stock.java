package leetcode;

public class Q_121_buy_sell_stock {
    public static int maxProfit(int[] prices) {
        int first = 0;
        int second = 1;
        int profit = 0;

        while (second < prices.length) {
            int temp = prices[second] - prices[first];

            if (prices[second] > prices[first])
                profit = Math.max(profit, prices[second] - prices[first]);
            else{
                first = second;
            }
            second ++;
        }
        return profit;
    }

    public static void main(String[] args){
        int[] stocks = {7,1,5,3,6,4};
        System.out.println(maxProfit(stocks));
    }
}
