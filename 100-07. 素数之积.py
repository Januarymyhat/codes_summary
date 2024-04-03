import math

num = int(input())


def is_primes(number):
    if number <= 1:
        return False
    for n in range(2, int(math.sqrt(number)) + 1):
        '''
        我们只需要考虑到不大于 num 的整数范围内的因子，因为如果一个数是合数，它的最小质因数肯定不会超过其平方根。
            假设我们有一个数 N，它的一个合数因子 A，那么 N = A * B，其中 B 是 N 的另一个因子。
            如果 A 和 B 都比 sqrt(N) 大，那么 A * B 的结果就会比 N 大，这与我们前提的 N = A * B 矛盾。
            所以，我们只需找到 num 的平方根即可，然后遍历到其平方根即可得到所有可能的质因数。

        int(math.sqrt(num)):平方根后取整。这个值表示了我们需要检查的最大可能的因子
        +1:为了确保在取整后覆盖到目标值，因为 range() 函数是不包含终止值的，因此需要额外加1
        '''
        if number % n == 0:
            return False
    return True


for i in range(2, int(math.sqrt(num)) + 1):
    if is_primes(i) and num % i == 0:
        if is_primes(num//i):
            print(i, num//i)
            break
else:
    print(-1, -1)


