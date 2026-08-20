# LPYAS70B

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

Write a program that takes two space separated inputs - the age (an integer) and the name of country(a string) and does the following:

- Prints "Eligible" if the age is greater than or equal to 18 and country is India
- Prints "Not Eligible", otherwise.

Check the sample input / output below for further clarity.

### Sample 1:
Input
Output

```
21 India
```

```
Eligible
```

### Sample 2:
Input
Output

```
16 India
```

```
Not Eligible
```

### Sample 3:
Input
Output

```
23 Nepal
```

```
Not Eligible
```

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-20T14:10:11.730Z  

```py
# cook your dish here
age,country=input().split()
age=int(age)
if age>=18 and country =="India":
    print("eligible")
else:
    print("not eligible")

```

---

[View on CodeChef](https://www.codechef.com/problems/LPYAS70B)