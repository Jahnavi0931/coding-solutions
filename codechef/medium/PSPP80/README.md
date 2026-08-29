# PSPP80

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

_Description not available._

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-29T16:49:52.894Z  

```py
def compute_value(a, b):
    # Solution as follows
    c = a*a + 2*a*b + b*b
    d = a + b
    print(c)
    print(d)

t = 3
for _ in range(t):
    A, B = map(int, input().split())
    compute_value(A, B)

```

---

[View on CodeChef](https://www.codechef.com/problems/PSPP80)