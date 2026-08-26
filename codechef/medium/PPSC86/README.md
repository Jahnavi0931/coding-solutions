# PPSC86

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

### Sum of N Integers

Listen

Chef was given an integer input N.

He wants to write a code using `while` loops to output the sum of all integers from 1 to $N$.
Help him complete the code by filling in the blanks.

### Sample 1:
Input
Output

```
5
```

```
15
```

### Sample 2:
Input
Output

```
10
```

```
55
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-26T17:47:59.270Z  

```py
# Solution as follows

n = int(input())
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1
    
print(sum)
```

---

[View on CodeChef](https://www.codechef.com/problems/PPSC86)