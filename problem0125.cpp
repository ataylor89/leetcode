class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty() || s.length() == 1)
            return true;
        
        string t;
        
        for (int i = 0; i < s.length(); i++) {
            if (isalnum(s[i])) {
                t += tolower(s[i]);
            }
        }
        
        for (int i = 0; i < t.length() / 2; i++) {
            if (t[i] != t[t.length()-i-1]) {
                return false;
            }
        }
        
        return true;
    }
};
