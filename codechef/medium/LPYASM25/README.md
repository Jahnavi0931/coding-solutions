# LPYASM25

![Difficulty](https://img.shields.io/badge/Difficulty-Medium-yellow)

## Problem

You are given two 24-hour format times as integers:
time1 = 1430 (2:30 PM)
time2 = 1615 (4:15 PM)

You need to calculate the difference between time2 and time1 in minutes using only operators.
Print the difference to the console.

## Solution

**Language:** Python  
**Runtime:** N/A  
**Memory:** N/A  
**Submitted:** 2026-08-06T13:11:42.151Z  

```py
# cook your dish here
time1=1430
time2=1615
minutes1=(time1//100)*60+(time1%100)
minutes2=(time2//100)*60+(time2%100)
difference=minutes2-minutes1
print(difference)
```

---

[View on CodeChef](https://www.codechef.com/problems/LPYASM25)