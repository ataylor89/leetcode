using namespace std;
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        string s = bitset<32>(n).to_string();
        int len = s.length();
        
        for (int i = 0; i < len/2; i++) {
            char tmp = s[i];
            s[i] = s[len - 1 - i];
            s[len - 1 - i] = tmp;
        }
        
        return bitset<32>(s).to_ulong();
    }
};
