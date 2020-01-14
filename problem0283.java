class Solution {
    public void moveZeroes(int[] nums) {
        if (nums.length < 2)
            return;
        
        for (int i = 0; i < nums.length; i++) {
            int maxOps = nums.length - i - 1;
            int counter = 0;
            while (nums[i] == 0 && counter < maxOps) {
                for (int j = i + 1; j < nums.length; j++) {
                    nums[i + (j-i-1)] = nums[j];
                }
                nums[nums.length-1] = 0;
                counter++;
            }
        }
    }
}
