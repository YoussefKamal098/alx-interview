# Prime Game

## Overview

The **Prime Game** is a competitive challenge where two players, Maria and Ben, take turns removing prime numbers and their multiples from a set of consecutive integers (from 1 to _n_). The twist is that each move corresponds to selecting a prime number, and the number of moves available in a game is equal to the number of prime numbers up to _n_. Maria always starts first, and if the total number of moves is odd, Maria wins the round; if even, Ben wins. The overall winner is determined by who wins the most rounds after _x_ rounds are played.

---

## Project Description

This project involves implementing the function `isWinner(x, nums)` in Python. The function simulates _x_ rounds of the Prime Game. In each round, the game is played on a set of numbers from 1 to _n_ (with each _n_ provided in the list `nums`). Using the Sieve of Eratosthenes to quickly count prime numbers, the function determines the winner for each round and then returns the overall winner:
- **Maria** wins a round if the number of prime numbers (moves) is odd.
- **Ben** wins if the number of moves is even.
- If the number of wins is tied or if invalid input is provided, the function returns `None`.

---

## Concepts Needed

To solve this problem, you should have a good grasp of the following topics:

### Prime Numbers
- **Definition:** Understanding what constitutes a prime number.
- **Identification:** Efficient algorithms (e.g., Sieve of Eratosthenes) to identify prime numbers up to a given limit.

### Sieve of Eratosthenes
- **Usage:** An algorithm to precompute prime numbers efficiently.
- **Benefit:** Reduces the time complexity when counting primes for each game round.

### Game Theory
- **Turn-based games:** Strategies where players make optimal moves.
- **Win conditions:** Understanding how the parity (odd or even) of the number of moves affects the outcome.

### Python Programming
- **Basic constructs:** Loops, conditionals, and list manipulations.
- **Arrays and Prefix Sums:** Using cumulative arrays to store counts for efficient lookup.

### Algorithm Optimization
- **Efficiency:** Precomputing primes and using a prefix sum array to handle multiple rounds quickly.

---

## Requirements

### General
- **Operating System:** Ubuntu 20.04 LTS.
- **Python Version:** Python 3.4.3.
- **PEP 8 Compliance:** All code must adhere to PEP 8 style guidelines.
- **Execution:** All Python files must be executable, with the first line as `#!/usr/bin/python3`.
- **Documentation:** A `README.md` file is required at the root of the project.

### Task Details
- **Function Prototype:**  
  ```python
  def isWinner(x, nums):
  ```
- **x:** An integer representing the number of rounds.
- **nums:** A list of integers, where each integer _n_ represents a round played on numbers from 1 to _n_.
- **Return Value:**  
  The function should return:
    - `"Maria"` if Maria wins more rounds,
    - `"Ben"` if Ben wins more rounds,
    - `None` if the winner cannot be determined (e.g., a tie or invalid input).

---

## Implementation Details

### Approach

1. **Prime Number Computation:**
    - Use the **Sieve of Eratosthenes** to compute all prime numbers up to the maximum value found in `nums`.

2. **Cumulative Prime Count:**
    - Create a prefix sum array where each index _i_ stores the count of prime numbers from 1 to _i_. This allows for fast lookup of the number of moves (prime numbers) for any round.

3. **Game Simulation:**
    - For each round (each value _n_ in `nums`), determine the number of moves.
    - If the number of moves is odd, count it as a win for Maria; if even, count it as a win for Ben.

4. **Overall Winner:**
    - After processing all rounds, compare the wins.
    - Return `"Maria"` if Maria wins more rounds, `"Ben"` if Ben wins more rounds, or `None` if the wins are equal.

### File Structure
- **GitHub Repository:** `alx-interview`
- **Directory:** `0x0A-primegame`
- **File:** `0-prime_game.py`

---

## Example

### Input
```python
x = 3
nums = [4, 5, 1]
```

### Round-by-Round Analysis
- **First Round (n = 4):**
    - Prime numbers: [2, 3] → 2 moves (even) → **Ben wins**.

- **Second Round (n = 5):**
    - Prime numbers: [2, 3, 5] → 3 moves (odd) → **Maria wins**.

- **Third Round (n = 1):**
    - No primes → 0 moves (even) → **Ben wins**.

### Expected Output
```bash
Winner: Ben
```

**Example Execution:**
```bash
$ ./main_0.py
Winner: Ben
```

---

## Resources

1. **Prime Numbers and Sieve of Eratosthenes:**
    - [Khan Academy: Prime Numbers](https://www.khanacademy.org/math/pre-algebra/integers)
    - [Sieve of Eratosthenes Explained](https://www.geeksforgeeks.org/sieve-of-eratosthenes/)

2. **Game Theory Basics:**
    - [Introduction to Game Theory](https://www.investopedia.com/terms/g/gametheory.asp)

3. **Dynamic Programming:**
    - [Dynamic Programming Concepts in Python](https://www.geeksforgeeks.org/python-dynamic-programming/)

4. **Python Official Documentation:**
    - [Python Lists](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists)

---

## Testing

### Sample Test Case
```python
# Sample test file: main_0.py
#!/usr/bin/python3
from 0-prime_game import isWinner

# Example test case
print("Winner:", isWinner(5, [2, 5, 1, 4, 3]))
# Expected output: Winner: Ben
```

Run the test using:
```bash
$ ./main_0.py
```

---

Happy coding! 🚀
