def guard(arr, N):
    # 상하좌우 방향 배열 (오른쪽, 왼쪽, 위, 아래 순서)
    dy = [0, 0, -1, 1] 
    dx = [1, -1, 0, 0]

    # 격자를 돌면서 경비원 위치 찾기
    for y in range(N):
        for x in range(N):
            if arr[y][x] == 2:  # 경비원을 발견하면
                # 네 방향으로 레이 캐스팅 시작
                for d in range(4):  
                    # 한 칸씩 멀어지며 탐색
                    for k in range(1, N):  
                        ny = y + dy[d] * k
                        nx = x + dx[d] * k

                        # 범위를 벗어나면 그 방향 종료
                        if ny < 0 or ny >= N or nx < 0 or nx >= N:
                            break  
                        # 벽(1)을 만나면 그 칸은 감시 불가, 그 방향도 종료
                        if arr[ny][nx] == 1:
                            break 
                        # 빈칸(0)이면 감시됨 → 마킹(여기서는 9로 표시)
                        if arr[ny][nx] == 0:
                            arr[ny][nx] = 9 
                # 경비원 칸도 마킹해서(9) 나중에 0으로 세지지 않게 함
                arr[y][x] = 9 

    # 모든 감시 처리 후 남아있는 0(=감시 못한 칸) 개수를 센다
    cnt = sum(row.count(0) for row in arr)
    return cnt

# 메인 실행부
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = guard(arr, N)
    print(f"#{tc} {result}")
