def knapsack_dp(values, weights, max_capacity):
    n = len(values)
    dp = [[0] * (max_capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, max_capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w-weights[i-1]])
            else:
                dp[i][w] = dp[i-1][w]

    items_included = []
    w = max_capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            items_included.append(1)
            w -= weights[i-1]
        else:
            items_included.append(0)
    items_included.reverse()

    return items_included, dp[n][max_capacity]

def knapsack_greedy(values, weights, max_capacity):
    n = len(values)
    items = sorted(((values[i], weights[i]) for i in range(n)), key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    capacity_used = 0
    items_included = [0] * n

    for value, weight in items:
        if capacity_used + weight <= max_capacity:
            index = values.index(value)
            items_included[index] = 1
            capacity_used += weight
            total_value += value

    return items_included, total_value

def knapsack_unbounded_greedy(values, weights, capacity):
    n = len(values)
    ratios = [(values[i] / weights[i], i) for i in range(n)]
    ratios.sort(reverse=True)

    total_value = 0
    selected_items = []
    current_weight = 0

    while current_weight < capacity:
        added = False
        for ratio, i in ratios:
            if weights[i] <= capacity - current_weight:
                total_value += values[i]
                selected_items.append(i)
                current_weight += weights[i]
                added = True
        if not added:
            break

    return total_value, selected_items

def knapsack_unbounded_dynamic(values, weights, capacity):
    n = len(values)
    dp = [0] * (capacity + 1)

    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                dp[w] = max(dp[w], values[i] + dp[w - weights[i]])

    selected_items = []
    w = capacity
    while w > 0:
        for i in range(n):
            if weights[i] <= w and dp[w] == values[i] + dp[w - weights[i]]:
                selected_items.append(i)
                w -= weights[i]
                break

    return dp[capacity], selected_items

# Example usage
if __name__ == "__main__":
    values = [60, 100, 120]
    weights = [10, 20, 30]
    max_capacity = 50

    print("0/1 Knapsack Problem using Dynamic Programming:")
    items_included, max_value = knapsack_dp(values, weights, max_capacity)
    print("Items included:", items_included)
    print("Maximum value achievable:", max_value)

    print("\n0/1 Knapsack Problem using Greedy Approach:")
    items_included, total_value = knapsack_greedy(values, weights, max_capacity)
    print("Items included:", items_included)
    print("Total value of items included:", total_value)

    print("\nUnbounded Knapsack Problem using Greedy Approach:")
    total_value, selected_items = knapsack_unbounded_greedy(values, weights, 100)
    print("Total value:", total_value)
    print("Selected items (zero-based index):", selected_items)

    print("\nUnbounded Knapsack Problem using Dynamic Programming:")
    max_value, selected_items = knapsack_unbounded_dynamic(values, weights, 100)
    print("Maximum value at full capacity:", max_value)
    print("Selected items (zero-based index):", selected_items)
