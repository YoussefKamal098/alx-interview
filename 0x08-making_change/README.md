### **README.md for "0. Change comes from within" Project**

---

# **0. Change Comes From Within**

## **Project Overview**
In this project, you will solve the classic **Coin Change Problem**, a problem from dynamic programming and greedy algorithms. The goal is to find the **fewest number of coins** required to make up a given total amount using an infinite supply of coins from a set of given denominations.

The project challenges you to apply your understanding of algorithms to devise an efficient solution, keeping in mind the limitations of greedy algorithms and when to use dynamic programming.

## **Project Requirements**
1. **Allowed Editors**: vi, vim, emacs
2. **Operating System**: Ubuntu 20.04 LTS
3. **Python Version**: Python 3.4.3 or higher
4. **Code Style**: PEP 8 compliant
5. **File Execution**: All Python files must be executable.
6. **File Naming**: The first line of all files should be `#!/usr/bin/python3`.

## **Problem Statement**
You are given a list of coin denominations, and a total amount. Your task is to find the minimum number of coins required to meet the total amount, using any number of coins from the given denominations.

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
In the greedy algorithm, we aim to use the largest denominations first to reduce the total as quickly as possible. This approach works optimally in many cases, but it may fail in cases where a better solution exists with smaller denominations.

```python
#!/usr/bin/python3
"""
Determines the minimum number of coins required to meet a given total amount.
"""

def makeChange(coins, total):
    """
    Function to determine the minimum number of coins required to meet a total.
    
    Args:
        coins (list): List of coin denominations (positive integers).
        total (int): Target amount to achieve.
        
    Returns:
        int: Minimum number of coins required to meet the total.
             Returns 0 if the total is 0 or less.
             Returns -1 if the total cannot be met with the given coins.
    """
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

### **Testing the Code**:
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
- Sorting the list of coins takes `O(n log n)`, where `n` is the number of different coin denominations.
- The loop that iterates through the sorted coins list runs in `O(n)` time, where `n` is the number of coins.
- The total time complexity is **O(n log n)**.

### **Space Complexity**:
- The space complexity is **O(1)** because the solution only uses a few extra variables and doesn't depend on the input size.

### **Dynamic Programming Alternative**:
If a greedy approach is not suitable for some coin sets, a dynamic programming solution can be used:

```python
def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for x in range(coin, total + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
```

This dynamic programming approach ensures that the solution is always optimal, but it has a higher time and space complexity of **O(n * total)**, where `n` is the number of coins and `total` is the target amount.

---

## **Conclusion**
- The solution to the coin change problem depends on the type of coin denominations.
- The greedy algorithm works well for standard coin sets but may fail in certain cases, for which a dynamic programming solution should be applied.
- Understanding when to use which algorithm is key to optimizing for both correctness and efficiency.

---
