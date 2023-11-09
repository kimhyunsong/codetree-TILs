n, b = map(int,input().split())
answer = 0

p, q = [], []
for _ in range(n):
    __, ___ = map(int,input().split())
    p.append(__)
    q.append(___)


for i in range(n):
    tmp_arr = []
    for j in range(n):
        if i == j:
            tmp_arr.append(p[j]// 2 + q[j])
        else:
            tmp_arr.append(p[j]+q[j])
    tmp_arr.sort()
    tmp_sum = 0
    for _ in range(n):
        if tmp_sum + tmp_arr[_] > b:
            break
        tmp_sum += tmp_arr[_]
    answer = (max(_, answer))
print(answer)