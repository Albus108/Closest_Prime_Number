# Closest Prime Function

A Python program that determines whether an integer is prime and, if it isn't, finds the closest prime number(s) to it.

## Features

- **Prime Detection:** Determines whether a given integer is prime.
- **Square Root Optimization:** Uses the square root of the input as the upper limit for divisor checking.
- **Odd Divisor Optimization:** Skips even divisors to reduce unnecessary iterations.
- **Bidirectional Search:** Searches both upwards and downwards to find the closest prime numbers.
- **Tie Detection:** Identifies when two prime numbers are equally close to the input.
- **Edge Case Handling:** Accounts for cases involving the smallest prime number, 2.

## How It Works

### 1. Prime Checking

The `P(n)` function checks whether an integer is prime.

It:
1. Rejects numbers smaller than 2.
2. Handles 2 as a special case.
3. Eliminates even numbers.
4. Checks only odd divisors up to the square root of the input.

### 2. Closest Prime Search

If the input is not prime, the program searches in both directions.

- For even inputs, it starts at `x + 1` and `x - 1`.
- For odd inputs, it starts at `x + 2` and `x - 2`.
- It skips even candidates by incrementing or decrementing by 2.
- It compares the distances to determine the closest prime number(s).

### 3. Result Comparison

The program compares the distances between the input and the nearest prime candidates.

- If the upper prime is closer, it prints the upper prime.
- If the lower prime is closer, it prints the lower prime.
- If both are equally distant, it prints both.

## Example

**Input:**
```text
x: 10
```

**Output:**
```text
Closest prime number to 10 is 11
```

Another example:

**Input:**
```text
x: 4
```

**Output:**
```text
Closest prime numbers to 4 are 5 and 3
```

## Requirements

- Python 3.x
- No external libraries required.

## How to Run

1. Clone this repository:
```bash
git clone <repository-url>
```

2. Navigate to the project directory.

3. Run the Python file:
```bash
python closest_prime.py
```

4. Enter an integer when prompted.

## Future Improvements

- Implement the **6k ± 1 optimization** for faster primality testing.
- Improve performance for extremely large integers.
- Benchmark different primality-testing algorithms.
- Explore more advanced prime-search techniques.
