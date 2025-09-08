# 0(사무실) 출발 → 1,2,3을 모두 방문 후 0으로 복귀하는 최소 비용
arr = [
    [0, 10, 15, 20],
    [5,  0,  9, 10],
    [6, 13, 0,  12],
    [8,  8,  9,  0]
]
N = 4

used = [False]*N
used[0] = True
best = float('inf')

def dfs(level, now, cost):
    global best
    # 가지치기: 현재 비용이 이미 최솟값 이상이면 더 볼 필요 없음
    if cost >= best:
        return

    if level == N-1:                # 1..N-1 모두 방문 완료
        best = min(best, cost + arr[now][0])  # 마지막에 0으로 복귀 비용 포함!
        return

    for nxt in range(1, N):         # 0은 사무실이라 제외
        if not used[nxt]:
            used[nxt] = True
            dfs(level + 1, nxt, cost + arr[now][nxt])  # now -> nxt 비용 누적
            used[nxt] = False

dfs(0, 0, 0)  # level=0(사무실만 있음), now=0, cost=0
print('최소 비용 =', best)
 