class Solution {
    public boolean isHappy(int n) {
    int slow = n, fast = getNext(n);
    while (fast != 1 && slow != fast) {
        slow = getNext(slow);       // 慢指针走一步
        fast = getNext(getNext(fast)); // 快指针走两步
    }
    return fast == 1;
}

    private int getNext(int n) {
        int sum = 0;
        while (n > 0) {
            int digit = n % 10;
            sum += digit * digit;
            n /= 10;
        }
        return sum;
    }
}
