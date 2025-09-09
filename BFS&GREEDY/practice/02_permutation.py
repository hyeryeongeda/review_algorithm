# {1,2,3}에서 길이 M=2인 순열 만들기 예제
N, M = 3, 2
used = [False]*(N+1)
picked = []

def dfs(level):
    if level == M:
        print(*picked)
        return

    for x in range(1, N+1):       # branch = 1 ~ N
        if used[x]:               # 이미 쓴 숫자라면
            continue              # 건너뛰기

        used[x] = True            # 이 숫자 x를 선택했음 표시
        picked.append(x)          # 현재 경로에 추가
        dfs(level+1)              # 다음 단계로 들어가기 (레벨 +1)
        picked.pop()              # 방금 넣은 숫자를 다시 빼서 원상복구
        used[x] = False           # 사용 표시도 풀어줌 (다른 경로에서 다시 쓸 수 있도록)
    
dfs(0)