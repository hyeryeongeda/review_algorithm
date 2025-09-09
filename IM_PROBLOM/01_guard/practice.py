def guard(N,arr):
    dy = [0,0,-1,1]
    dx = [1,-1,0,0]
    cnt = 0
    for y in range(N):
        for x in range(N):
            if arr[y][x] ==2:
                for d in range(4):
                    for k in range(1, N):
                        ny = y + dy[d]*k
                        nx = x + dx[d]*k
                        if ny<0 or ny >= N or nx<0 or nx>= N:
                            break
                        if arr[ny][nx] == 1:
                            break
                        if arr[ny][nx] == 0:
                            arr[ny][nx] = 9
                arr[y][x] = 9
    cnt = sum(row.count(0) for row in arr)
    return cnt

T =int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    result = guard(N,arr)
    print(f'#{tc} {result}')