N, K = map(int, input().split())
commands = [list(map(int, input().split())) for _ in range(K)]
def solve(N, K, commands):
    blocks = [0] * (N + 1)
    for _ in range(K):
        Ai, Bi = commands[_]
        blocks[Ai] += 1
        if Bi + 1 <= N:
            blocks[Bi + 1] -= 1
    for i in range(1, N + 1):
        blocks[i] += blocks[i - 1]
    
    mid_index = N // 2
    mid_value = sorted(blocks)[mid_index]
    print(mid_value)


solve(N, K, commands)