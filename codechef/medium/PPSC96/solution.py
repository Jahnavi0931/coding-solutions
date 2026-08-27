N, M = map(int, input().split())

# Solution as follows
result = 1

# Calculate N to the power M
for i in range(M):
    result = N * result

print(result)
