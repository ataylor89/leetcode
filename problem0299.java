class Solution {
    public String getHint(String secret, String guess) {
        int bulls = 0;
        int cows = 0;
        
        Map<Character, Integer> available = new HashMap<>();
        
        for (int i = 0; i < secret.length(); i++) {
            Character c = secret.charAt(i);
            
            if (!available.containsKey(c))
                available.put(c, 1);
            
            else 
                available.put(c, available.get(c) + 1);
        }
        
        String possibleCows = "";
        
        for (int i = 0; i < secret.length(); i++) {
            Character a = secret.charAt(i);
            Character b = guess.charAt(i);
            
            if (a == b) {
                bulls++;
                
                available.put(a, available.get(a) - 1);
            }
            else 
                possibleCows += b;
        }
        
        for (int i = 0; i < possibleCows.length(); i++) {
            Character pc = possibleCows.charAt(i);
            
            if (available.containsKey(pc) && available.get(pc) > 0) {
                cows++;
                available.put(pc, available.get(pc) - 1);
            }
        }
        
        return String.format("%dA%dB", bulls, cows);
    }
}
