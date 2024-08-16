class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        map<string, vector<string>> dic;
        for (int i = 0; i < strs.size(); i++) {
            string sortedStr = strs[i]; 
            sort(sortedStr.begin(), sortedStr.end());
            dic[sortedStr].push_back(strs[i]);
        }
        vector<vector<string>> res;
        for (auto it = dic.begin(); it != dic.end(); ++it) {
            res.push_back(it->second);
        }
        return res;
    }
};