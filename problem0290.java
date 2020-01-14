class Solution {
    public boolean wordPattern(String pattern, String str) {
        String[] splt = str.split(" ");
        
        if (splt == null || pattern.length() != splt.length)
            return false;
        
        Map<Character, String> words = new HashMap<>();
        Map<String, Character> letters = new HashMap<>();
        
        for (int i = 0; i < pattern.length(); i++) {
            Character c = pattern.charAt(i);
            String word = splt[i];
            
            boolean hasLetter = words.containsKey(c);
            
            if (!hasLetter) {
                if (letters.containsKey(word)) 
                    return false;
                
                words.put(c, word);
                letters.put(word, c);
            }
            else if (!word.equals(words.get(c)))
                return false;
        }
                
        return true;
    }
}
