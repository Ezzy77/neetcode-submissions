class Solution {
    public boolean hasDuplicate(int[] nums) {
        /** 
        given an array of integers, check for duplicate
        to solve the problem we could use a naive approach 
        by using nested loop to compare.

        An optimal solution is to solve it with o(n) time and space complexity


        **/

        // naive approach
        // for(int i = 0; i < nums.length; i ++){
        //     for(int j = i + 1; j < nums.length; j++){
        //         if(nums[i] == nums[j]){
        //             return true;
        //         }
        //     }
        // }
        // return false;

        // the time complexity is 0(n^2) time due to the nested loop 

        // using HashSet for faster look up (O(1) times)

        HashSet<Integer> seen = new HashSet<>();

        for (int num : nums){
            if(seen.contains(num)){
                return true;
            }
            seen.add(num);
        }
        return false;


    }
}