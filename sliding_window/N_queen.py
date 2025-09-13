# 1. 열방향 used배열
used = [0] * 20
# 2. / 방향 대각선 used 배열
used1 = [0] * 100
# 3. \ 방향 대각션 used 배열
used2 = [0] * 100

def dfs(row):
    global cnt
    # 정점 노드에 도달했을때
    if row == N:
        cnt += 1
        return

    for col in range(N):
        # 열 방향 : 열방향에 queen이 있다
        if used[col] == 1: continue
        # / 방향 : /방향에 queen이 있다
        if used1[col + row] == 1: continue
        # \ 방향 : \방향에 queen이 있다.
        if used2[col - row + N] == 1: continue

        used[col] = 1
        used1[col + row] = 1
        used2[col - row + N] = 1

        dfs(row + 1)

        used[col] = 0
        used1[col + row] = 0
        used2[col - row + N] = 0

cnt = 0
N = int(input())
dfs(0) # 0행부터 시작
print(cnt)

