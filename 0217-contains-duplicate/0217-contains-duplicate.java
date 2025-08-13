class Solution {
    public boolean containsDuplicate(int[] nums) {
        Map<Integer, Integer> numMap = new HashMap<>();

        for(int num: nums) {
            if (numMap.get(num) != null) return true;
            numMap.put(num, 1);
        }
        return false;
    }
}