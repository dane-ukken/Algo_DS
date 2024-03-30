public class Solution {
    public int CharacterReplacement(string s, int k) {
        int maxF = 0, res = 0, l = 0, r = 0;
        Dictionary<char, int> countDict = new Dictionary<char, int>();
        
        while(r < s.Length) {
            char c = s[r];
            if (!countDict.ContainsKey(c)) {
                countDict[c] = 0;
            }
            countDict[c] += 1;
            maxF = Math.Max(maxF, countDict[c]);
            
            while(r - l + 1 - maxF > k) {
                char cl = s[l];
                countDict[cl] -= 1;
                l += 1;
            }
            
            res = Math.Max(r - l + 1, res);
             r += 1;
        }
        return res;
    }
}