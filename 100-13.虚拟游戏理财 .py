products, N, X = map(int, input().split())
rate_of_return = list(map(int, input().split()))
risks = list(map(int, input().split()))
max_invest = list(map(int, input().split()))

'''
我们需要筛选出符合投资限制条件的所有可能的投资组合，然后计算它们的回报，从中选择最大的回报
'''

max_return = 0
best_allocation = [0] * products

for i in range(products):
    for j in range(i + 1, products):
        # 外层循环遍历第一种产品i，内层循环遍历第二种产品j，确保j大于i以避免重复计算
        investment_i = min(max_invest[i], N)
        investment_j = min(max_invest[j], N - investment_i)  # 考虑总投资额度不超过N
        if risks[i] + risks[j] <= X:
            # 外层循环遍历第一种产品i，内层循环遍历第二种产品j，确保j大于i以避免重复计算
            returns = investment_i * rate_of_return[i] + investment_j * rate_of_return[j]
            if returns > max_return:
                max_return = returns
                best_allocation = [0] * products
                best_allocation[i] = investment_i
                best_allocation[j] = investment_j

print(best_allocation)
