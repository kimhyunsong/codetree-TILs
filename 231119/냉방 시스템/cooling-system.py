from collections import deque
n, m, k = map(int, input().split())
office = [list(map(int, input().split())) for _ in range(n)]
condition = [[0] * n for _ in range(n)]
selected_office = []
m_location = []
possible_office = []
for i in range(n):
    for j in range(n):
        if office[i][j] == 1:
            selected_office.append((i, j))
        if office[i][j] >= 2:
            m_location.append((i, j, office[i][j]))


walls = []
for _ in range(m):
    i, j, __ = list(map(int, input().split()))
    walls.append([i - 1, j - 1, __])


def check():
    global minute
    global k
    for i, j in selected_office:
        if condition[i][j] < k:
            return 1
    else:
        print(minute)

        return 0



# left up right down
def is_possible(r, c, dir):
    key = True
    for wr, wc, d in walls:
        if dir == 0:
            if c - 1 < 0 or (r == wr and c == wc and d == 1):
                key = False
                break
        elif dir == 1:
            if r - 1 < 0 or (r == wr and c == wc and d == 0):
                key = False
                break
        elif dir == 2:
            if c + 1 >= n or (r== wr and c + 1 == wc and d == 1):
                key = False
                break
        elif dir == 3:
            if r + 1 >= n or (r + 1 == wr and c == wc and d == 0):
                key = False
                break
    return key


def spread(m):
    r, c, dir = m
    power = 5
    visited = [[False] * n for _ in range(n)]
    space = deque()
    if dir == 2:
        space.append((r, c - 1, power))
        while space:
            nr, nc, p = space.popleft()
            if p == 0: continue
            condition[nr][nc] += p
            if possible_office[nr][nc][1] and possible_office[nr - 1][nc][0] and not visited[nr - 1][nc - 1]:
                visited[nr - 1][nc - 1] = True
                space.append((nr - 1, nc - 1, p - 1))
            if possible_office[nr][nc][0] and not visited[nr][nc - 1]:
                visited[nr][nc - 1] = True
                space.append((nr, nc - 1, p - 1))
            if possible_office[nr][nc][3] and possible_office[nr + 1][nc][0] and not visited[nr + 1][nc - 1]:
                visited[nr + 1][nc - 1] = True
                space.append((nr + 1, nc - 1, p - 1))
    if dir == 3:
        space.append((r - 1, c, power))
        while space:
            nr, nc, p = space.popleft()
            if p == 0: continue
            condition[nr][nc] += p
            if possible_office[nr][nc][0] and possible_office[nr][nc - 1][1] and not visited[nr - 1][nc - 1]:
                visited[nr - 1][nc - 1] = True
                space.append((nr - 1, nc - 1, p - 1))
            if possible_office[nr][nc][1] and not visited[nr - 1][nc]:
                visited[nr - 1][nc] = True
                space.append((nr - 1, nc,  p - 1))
            if possible_office[nr][nc][2] and possible_office[nr][nc + 1][1] and not visited[nr - 1][nc + 1]:
                visited[nr - 1][nc + 1] = True
                space.append((nr - 1, nc + 1, p - 1))
    if dir == 4:
        space.append((r, c + 1, power))
        while space:
            nr, nc, p = space.popleft()
            if p == 0: continue
            condition[nr][nc] += p
            if possible_office[nr][nc][1] and possible_office[nr - 1][nc][2] and not visited[nr - 1][nc + 1]:
                visited[nr - 1][nc + 1] = True
                space.append((nr - 1, nc + 1, p - 1))
            if possible_office[nr][nc][2] and not visited[nr][nc + 1]:
                visited[nr][nc + 1] = True
                space.append((nr, nc + 1, p - 1))
            if possible_office[nr][nc][3] and possible_office[nr + 1][nc][2] and not visited[nr + 1][nc + 1]:
                visited[nr + 1][nc + 1] = True
                space.append((nr + 1, nc + 1, p - 1))
    if dir == 5:
        space.append((r + 1, c, power))
        while space:
            nr, nc, p = space.popleft()
            if p == 0: continue
            condition[nr][nc] += p
            if possible_office[nr][nc][0] and possible_office[nr][nc - 1][3] and not visited[nr + 1][nc - 1]:
                visited[nr + 1][nc - 1] = True
                space.append((nr + 1, nc - 1, p - 1))
            if possible_office[nr][nc][3] and not visited[nr + 1][nc]:
                visited[nr + 1][nc] = True
                space.append((nr + 1, nc,  p - 1))
            if possible_office[nr][nc][2] and possible_office[nr][nc + 1][3] and not visited[nr + 1][nc + 1]:
                visited[nr + 1][nc + 1] = True
                space.append((nr + 1, nc + 1, p - 1))

for i in range(n):
    tmp_row = []
    for j in range(n):
        tmp_idx = []    
        for _ in range(4):
            tmp_idx.append(is_possible(i, j, _))
        tmp_row.append(tmp_idx)
    possible_office.append(tmp_row)
idx_arr = [[0, -1], [-1 ,0], [0, 1], [1, 0]]

def mix():
    tmp = []
    for i in range(n):
        for j in range(n):
            for k in range(len(idx_arr)):
                if possible_office[i][j][k]:
                    nr, nc = i + idx_arr[k][0], j + idx_arr[k][1]
                    if condition[i][j] - condition[nr][nc] >= 4:
                        val = (condition[i][j] - condition[nr][nc]) // 4
                        tmp.append((i, j, -val, nr, nc, val))
    for i, j, val1, nr, nc, val2 in tmp:
        condition[i][j] += val1
        condition[nr][nc] += val2
    
    return

def cool_down(n):
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n - 1 or j == 0 or j == n - 1) and condition[i][j] > 0:
                condition[i][j] -= 1

minute = 0
while check():
    if minute >= 100:
        print(-1)
        break
    for m in m_location:
        spread(m)
        
    mix()

    cool_down(n)
    minute += 1