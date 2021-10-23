// Solution 1: HashMap key takes ** sorted string **
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> strGroup = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            char[] chars = strs[i].toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);
            if (strGroup.containsKey(sorted) == false) {
                List<String> tmp = new ArrayList<>();
                tmp.add(strs[i]);
                strGroup.put(sorted, tmp);
            } else {
                strGroup.get(sorted).add(strs[i]);
            }
        }
        List<List<String>> ans = new ArrayList<>();
        for (String str : strGroup.keySet()) {
            ans.add(strGroup.get(str));
        }
        return ans;
    }
}


// Solution 2: HashMap key takes ** char index **
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> strGroup = new HashMap<>();
        for (int i = 0; i < strs.length; i++) {
            String charArray = stringToCharArray(strs[i]);
            if (strGroup.containsKey(charArray) == false) {
                List<String> tmp = new ArrayList<>();
                tmp.add(strs[i]);
                strGroup.put(charArray, tmp);
            } else {
                strGroup.get(charArray).add(strs[i]);
            }
        }
        List<List<String>> ans = new ArrayList<>(strGroup.values());
        return ans;
    }

    private String stringToCharArray(String str) {
        int[] chars = new int[26];
        for (int i = 0; i < str.length(); i++) {
            chars[str.charAt(i) - 'a'] += 1;
        }
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < chars.length; i++) {
            if (chars[i] > 0) {
                // 只记录出现次数会误判，示例 ["bdddddddddd","bbbbbbbbbbc"]
                // 因此需要同时记录出现的字母
                sb.append(i + 'a');
                sb.append(chars[i]);
            }
        }
        return sb.toString();
    }
}
