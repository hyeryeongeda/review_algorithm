def dfs(y, x, sum_v):
    """
    y, x  : 현재 위치 (좌표)
    sum_v : 지금까지 이동하면서 더한 비용의 합
    min_sum : 지금까지 찾은 최소 비용 (전역 변수)
    """

    # 2. 기저 조건: (y, x)가 맨 끝칸(N-1, N-1)에 도달한 경우
    #   → 지금까지 계산한 경로 합(sum_v)과 현재까지의 최소값(min_sum)을 비교해서 더 작은 값으로 갱신
    if y == N - 1 and x == N - 1:
        global min_sum
        min_sum = min(min_sum, sum_v)
        return

    # 3. 가지치기(pruning): 이미 지금까지의 합이 현재 최소값 이상이면
    #    더 내려가봤자 최소값을 갱신할 수 없으므로 탐색 중단
    if sum_v >= min_sum:
        return

    # 1. 다음 선택(branch) → 현재 위치에서 오른쪽(x+1) 또는 아래(y+1)로만 이동 가능
    #   그래서 branch를 두 가지로 나눔:
    #   1-1. 오른쪽으로 이동 (x+1)
    if x < N - 1:  # 오른쪽 끝이 아닐 때만 가능
        dfs(y, x + 1, sum_v + arr[y][x + 1])

    #   1-2. 아래로 이동 (y+1)
    if y < N - 1:  # 맨 아래줄이 아닐 때만 가능
        dfs(y + 1, x, sum_v + arr[y + 1][x])


T = int(input())  # 테스트 케이스 개수
for tc in range(1, T + 1):
    N = int(input())  # 격자 크기
    arr = [list(map(int, input().split())) for _ in range(N)]  # N x N 배열 입력
    min_sum = float('inf')  # 최소 비용을 무한대로 초기화

    # 시작점은 (0,0), 첫 칸 비용은 arr[0][0]
    dfs(0, 0, arr[0][0])

    # 결과 출력
    print(f'#{tc} {min_sum}')
