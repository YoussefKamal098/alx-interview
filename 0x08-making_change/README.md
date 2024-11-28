# Making Change Problem

## **Project Overview**
In this project, you will solve the classic **Coin Change Problem**, a problem from dynamic programming. The goal is to find the **fewest number of coins** required to make up a given total amount using an infinite supply of coins from a set of given denominations.

This project challenges you to apply your understanding of dynamic programming and greedy algorithms, highlighting the limitations of the greedy approach and how dynamic programming provides a more reliable solution.

## **Project Requirements**
1. **Allowed Editors**: vi, vim, emacs
2. **Operating System**: Ubuntu 20.04 LTS
3. **Python Version**: Python 3.4.3 or higher
4. **Code Style**: PEP 8 compliant
5. **File Execution**: All Python files must be executable.
6. **File Naming**: The first line of all files should be `#!/usr/bin/python3`.

## **Problem Statement**
You are given a list of coin denominations and a total amount. Your task is to find the minimum number of coins required to meet the total amount, using any number of coins from the given denominations.

### **Prototype**:
```python
def makeChange(coins, total):
```

- **Arguments**:
    - `coins`: A list of integers representing coin denominations.
    - `total`: An integer representing the target total amount.

- **Returns**:
    - The minimum number of coins needed to meet the total.
    - `0` if the total is less than or equal to 0.
    - `-1` if the total cannot be achieved with the given denominations.

---

## **Algorithm Solution**

### **Greedy Approach**:
The greedy algorithm aims to use the largest denominations first to reduce the total as quickly as possible. While this approach works optimally in many cases, it may fail in situations where a better solution exists using smaller denominations.

For example:
- With coins `[1, 2, 5]`, for a total of `6`, the greedy approach would give you `1 coin of 5 + 1 coin of 1`, which results in `2 coins`. But the optimal solution is `3 coins of 2`.

Thus, **the greedy approach does not always work** for all cases. We need a more robust solution like dynamic programming.

```python
#!/usr/bin/python3
def makeChange(coins, total):
    if total <= 0:
        return 0

    coins.sort(reverse=True)  # Sort coins in descending order for greedy approach
    count = 0

    for coin in coins:
        if total <= 0:
            break
        num_coins = total // coin
        count += num_coins
        total -= num_coins * coin

    return count if total == 0 else -1
```

---

## **Dynamic Programming Solution**:

The **dynamic programming (DP)** approach is the correct solution to this problem. It ensures that the result is optimal by considering all possible ways to reach the total, using the minimum number of coins. 

- **Iterative DP Solution**:
The iterative solution builds up the minimum number of coins for each amount from `0` to the target total.

```python
def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # No coins needed to make 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
```

- **Recursive DP Solution**:
A recursive approach can be used with memoization to store previously computed results, thus avoiding redundant calculations.

```python
def makeChange(coins, total):
    def dp_recursive(coins, total, memo):
        if total == 0:
            return 0
        if total < 0:
            return float('inf')
        if total in memo:
            return memo[total]

        min_coins = float('inf')
        for coin in coins:
            res = dp_recursive(coins, total - coin, memo)
            if res != float('inf'):
                min_coins = min(min_coins, res + 1)

        memo[total] = min_coins
        return min_coins

    if total <= 0:
        return 0

    result = dp_recursive(coins, total, {})
    return result if result != float('inf') else -1
```

---

## **Testing the Code**:
Create a test file `0-main.py`:

```python
#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

# Test cases
print(makeChange([1, 2, 25], 37))  # Expected output: 7 (25 + 10 + 2)
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Expected output: -1
print(makeChange([1, 5, 10, 25], 0))  # Expected output: 0
print(makeChange([5, 10, 25], 3))  # Expected output: -1
```

---

## **Time and Space Complexity Analysis**

### **Time Complexity**:
- **Greedy Approach**: Sorting the list of coins takes `O(n log n)`, where `n` is the number of coin denominations. The loop to iterate over the coins is `O(n)`. Therefore, the total time complexity is **O(n log n)**.
- **Dynamic Programming**:
    - **Iterative DP**: The loop over coins and the inner loop for each total value give a time complexity of **O(n * total)**, where `n` is the number of coins and `total` is the target amount.
    - **Recursive DP**: The recursive solution has a time complexity of **O(n * total)**, where memoization reduces the redundant work.

### **Space Complexity**:
- **Greedy Approach**: The space complexity is **O(1)** because only a few extra variables are used.
- **Dynamic Programming**:
    - **Iterative DP**: The space complexity is **O(total)** due to the `dp` array.
    - **Recursive DP**: The space complexity is **O(total)** due to the recursion stack and memoization.

---

### **Conclusion**
- The **greedy approach** is **not always reliable** and may fail in some cases (e.g., when the optimal solution requires using smaller denominations first).
- The **dynamic programming solution** ensures an optimal and reliable result, especially when the greedy approach fails.

