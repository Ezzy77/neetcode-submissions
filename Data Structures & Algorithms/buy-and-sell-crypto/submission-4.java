class Solution {
    public int maxProfit(int[] prices) {
        /**
        Brute force method, t = o(n^2), s = o(1);
        int maxProfit = 0;
        
        for(int i = 0; i < prices.length; i++){
            // initially buy at first day
            int buyPrice = prices[0];
            for (int j = i + 1; j < prices.length; j++){
                int sellPrice = prices[j];
                maxProfit = Math.max(maxProfit, sellPrice - buyPrice); 
            }
        }
        return maxProfit;
        **/

        // More efficient solution is using two pointer, left (buy) 
        // and right (sell)

        int left = 0, right = 1;
        int maxProfit = 0;

        while(right < prices.length){
            // if buy price is less than sell
            if(prices[left] < prices[right]){
                // compute profit
                int profit = prices[right] - prices[left];
                maxProfit = Math.max(maxProfit, profit);
            }else{
                left = right;
            }
            right++;
        }
        return maxProfit;
    }
}
