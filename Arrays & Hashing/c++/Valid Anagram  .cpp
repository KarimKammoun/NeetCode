class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char,int >dic1;
        map<char,int >dic2;
        for (int i=0;i<size(s);i++)
        {
            if (s[i])
            dic1[s[i]]=dic1+1
        }
        for (int i=0;i<size(t);i++)
        {
            dic2[s[i]]=dic2+1
        }
        if (dic1 == dic2 )
        {
            return true
        }
        else
            return false
        
    }
};