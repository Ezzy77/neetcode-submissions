// effective solution
class Solution {
    public boolean hasDuplicate(int[] nums) {
        // brute force solutiuon runs o(n2) and o(1) space
        // more efficient solution try to solve on single pass

        // using set for o(n) pass and on(n) space. however 
        // insertion and look up is o(1)

        Set<Integer> seen = new HashSet<>();

        for(int n : nums){
            if (seen.contains(n)){
                return true;
            }
            seen.add(n);
        }
        return false;
    }
}
