# level = 깊이(몇 번째 선택인가)
# branch = 현재 레벨에서 시도할 선택지들의 집합
picked = []

def dfs(level):
    if level == 3:          # 예: 3단계 선택이 끝나면 종료/사용
        print(picked)
        return

    for choice in ['A','B','C']:   # <- 이게 branch(선택지)
        picked.append(choice)       # 선택
        dfs(level + 1)              # 다음 단계(레벨)로
        picked.pop()                # 되돌리기(백트래킹)

dfs(0)
