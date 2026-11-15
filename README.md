# Closest Prime Number Finder

A program that determines whether a given integer is prime. If it isn't, the program finds the closest prime number or numbers to it.

Currently implemented in **Python** and **C++**.

## Features

- **Prime Detection:** Checks whether an integer is prime.
- **Square Root Optimization:** Limits divisor checks to the square root of the input.
- **Odd Divisor Optimization:** Skips even divisors to reduce unnecessary calculations.
- **Bidirectional Search:** Searches both above and below the input to find the closest prime.
- **Tie Detection:** Identifies when two prime numbers are equally close.
- **Edge Case Handling:** Handles cases involving the smallest prime number, 2.

## Implementations

| File | Language | Description |
|---|---|---|
| `closest prime function.py` | Python | Original implementation |
| `closest-prime.cpp` | C++ | C++ implementation of the same algorithm |

## How It Works

1. The program takes an integer as input.
2. It checks whether the number is prime.
3. If it is prime, the program reports it.
4. Otherwise, it searches for prime numbers above and below the input.
5. It compares their distances from the input.
6. It displays the closest prime number or both numbers if there is a tie.

## Running the Programs

### Python

Make sure Python is installed, then run:

```bash
python "closest prime function.py"
```

### C++

Compile using a C++ compiler such as g++:

```bash
g++ closest-prime.cpp -o closest-prime
```

Then run:

```bash
./closest-prime
```

On Windows, run:

```bash
closest-prime.exe
```

## Future Improvements

- Improve efficiency for very large integers.
- Explore more advanced prime-search algorithms.
- Refactor the program into smaller, reusable functions.
- Compare the performance of the Python and C++ implementations.

## Author

**Albus108**

