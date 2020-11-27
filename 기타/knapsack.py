def knapsack(k, w, v, n):
    if k <= 0 or n <= 0:
        return 0
    if w[n-1] > k:
        return knapsack(k, w, v, n-1)
    carry = v[n - 1] + knapsack(k - w[n-1], w, v, n-1)
    leave = knapsack(k, w, v, n-1)
    return max(carry, leave)

    # current_v = v[n-1]
    # current_w = w[n-1]
    # if current_w >= k:
    #     return
    # if n == 1:
    #     return v[0]
    # return max(knapsack(n-1, k, w, v), knapsack(n, k-current_w, w, v))
print(knapsack(50,[10,20,30],[60,100,120],3))