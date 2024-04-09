numbers = int(input())
abilities = list(map(int, input().split()))
limit = int(input())

abilities.sort()
groups = 0
i = 0
for i in range(len(abilities)):
    if abilities[i] >= limit:
        groups += 1
        # print("执行")
    else:
        for j in range(i+1, len(abilities)):
            if abilities[i] + abilities[j] >= limit:
                groups += 1
                abilities[j] = 0  # 更简单
                break
        '''
        summaries = {}
        for j in range(i+1, len(abilities)):
            summary = 0
            if abilities[i] + abilities[j] >= limit:
                summary = abilities[i] + abilities[j]
                summaries.update({j: summary})    

        min_summary = min(summaries, key=lambda x: summaries[x])
        print(f'min:{min_summary}')
        # abilities.pop(summaries[min_summary])  # 删除指定的键值对，最后返回的是删除键的值
        del abilities[min_summary]
        groups += 1
        '''

print(groups)
