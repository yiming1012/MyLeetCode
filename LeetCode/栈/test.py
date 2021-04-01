def dfs(num):
    if num <= 9:
        return num
    return dfs(num // 10) + num % 10


res = dfs(12345)
print(res)

res = 0
for i in range(1, 100, 2):
    res += i

for i in range(1, 100, 2):
    res += i / 10 if i < 10 else i / 100

print(res)
