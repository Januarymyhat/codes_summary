summary = int(input())
lucky_number = int(input())
command = list(map(int, input().split()))

result = [0]
position = 0

if (1 <= summary <= 100
        and -100 <= lucky_number <= 100):
    for cmd in command:
        # command 是一个列表，你需要使用 len() 函数来获取列表的长度，然后将长度作为 range() 函数的参数
        if -100 <= cmd <= 100:
            if cmd == lucky_number:
                position += cmd + (-1 if lucky_number < 0 else 1)
                # result += (-1 if lucky_number < 0 else 1)
            else:
                position += cmd
            result.append(position)
    print(max(result))
else:
    print(12345)

