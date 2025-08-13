class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List> strMap = new HashMap<>();

        for (String s: strs) {
            char[] c = s.toCharArray();
            Arrays.sort(c);
            String key = String.valueOf(c);
            if (!strMap.containsKey(key)) strMap.put(key, new ArrayList());
            strMap.get(key).add(s);
        }
        return new ArrayList(strMap.values());
    }
}