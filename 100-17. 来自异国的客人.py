k, n, m = map(int, input().split())
trans = ""
while k > 0:
    trans += str(k % m)
    k = k // m

print(trans.count(str(n)))

