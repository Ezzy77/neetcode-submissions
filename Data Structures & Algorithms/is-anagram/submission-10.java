class Solution {
    public boolean isAnagram(String s, String t) {
        // efficient solution using frequency map
        //  for this solution we create 2 hash map to store frequencies , then if check 
        // if two maps are equal (if they have number of char count)

        // first check if the two strings are same length

        if(s.length() != t.length()){
            return false;
        }

        Map<Character, Integer> sCount = new HashMap<>();
        Map<Character, Integer> tCount = new HashMap<>();

        for(int i=0; i<s.length(); i++){
            sCount.put(s.charAt(i), sCount.getOrDefault(s.charAt(i), 0) + 1);
            tCount.put(t.charAt(i), tCount.getOrDefault(t.charAt(i), 0) + 1);

        }

        return sCount.equals(tCount);
    }
}
