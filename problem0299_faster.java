class Solution {
    public String getHint(String secret, String guess) {
        int bulls = 0;
        int cows = 0;
        
        Map<Character, Integer> available = new HashMap<>();
        
        String possibleCows = "";
        
        for (int i = 0; i < secret.length(); i++) {
            Character a = secret.charAt(i);
            Character b = guess.charAt(i);
            
            if (a == b) {
                bulls++;
                continue;
            }
            
            if (!available.containsKey(a))
                available.put(a, 1);
            else
                available.put(a, available.get(a) + 1);
            
            possibleCows += b;
        }
        
        for (int i = 0; i < possibleCows.length(); i++) {
            Character c = possibleCows.charAt(i);
            
            if (available.containsKey(c) && available.get(c) > 0) {
                cows++;
                available.put(c, available.get(c) - 1);
            }
        }
        
        return String.format("%dA%dB", bulls, cows);
    }
}
