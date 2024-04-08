max_tasks = int(input())
array_length = int(input())
array = list(map(int, input().split()))


time = 0
temp = 0
for i in array:
    if i + temp >= max_tasks:
        temp = i + temp - max_tasks
    else:
        temp += i
    time += 1  # 添加任务后也需要+1s

while temp > 0:
    time += 1
    temp -= max_tasks
print(time)
