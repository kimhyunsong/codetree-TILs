n, k = map(int, input().split())
arr = [0]* n
tmp = []
for _ in range(k):
    p, q= map(int, input().split())
    for i in range(p, q + 1):
        arr[i- 1] += 1
arr.sort()

print(arr[len(arr)//2])