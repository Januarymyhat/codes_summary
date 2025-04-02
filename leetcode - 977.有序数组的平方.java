class Solution {
    public int[] sortedSquares(int[] nums) {
        int[] newNums = new int[nums.length]; 
        int right = nums.length-1;
        int left = 0;
        int index = newNums.length-1;
        while(left<=right){
            if(nums[left]*nums[left]<nums[right]*nums[right]){
                newNums[index--]=nums[right]*nums[right];
                right--; // 或者--right
            } else{
                newNums[index--]=nums[left]*nums[left];
                left++; // 或者++left
            }
        }
        return newNums;
    }
}
