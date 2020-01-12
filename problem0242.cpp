class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length())
            return false;
        
        map<char,int> s_map;
        map<char,int> t_map;
        
        for (int i = 0; i < s.length(); i++) {
            char chr_s = s[i];
            char chr_t = t[i];
            
            if (s_map.find(chr_s) == s_map.end())
                s_map[chr_s] = 1;
            else
                s_map[chr_s] += 1;
                
            if (t_map.find(chr_t) == t_map.end())
                t_map[chr_t] = 1;
            else
                t_map[chr_t] += 1;
        }
        
        map<char,int>::iterator it;
        for (it = s_map.begin(); it != s_map.end(); ++it) {
            char chr_s = it->first;
            int count_s = it->second;
            
            if (t_map.find(chr_s) == t_map.end()) 
                return false;
            
            int count_t = t_map[chr_s];
            
            if (count_s != count_t)
                return false;
        }
        return true;
    }
};
