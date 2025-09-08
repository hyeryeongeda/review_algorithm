# {1,2,3,4}에서 길이 M=2 조합 만들기 (오름차순 유지)
N, M = 4, 2      # 1부터 N까지의 수 중에서 M개를 고른다
picked = []      # 현재까지 선택한 숫자들을 담아둘 리스트

def dfs(level, start):
    # level: 현재까지 선택한 개수
    # start: 이번 단계에서 선택할 수 있는 최소 숫자 (오름차순 유지를 위해 필요)

    # 1. 원하는 개수(M)만큼 뽑았으면 출력하고 종료
    if level == M:
        print(*picked)     # 예: [1,2] → 출력: 1 2
        return

    # 2. 현재 단계에서 선택할 수 있는 후보는 start ~ N
    for x in range(start, N+1):   # ← 여기서 N 사용 (전체 숫자의 끝)
        picked.append(x)          # 숫자 x를 경로에 추가
        dfs(level + 1, x + 1)     # 다음 단계로 들어갈 때는 x+1부터 시작
                                   # → 이렇게 해야 오름차순만 남고 중복 방지됨
        picked.pop()              # 방금 추가한 x를 제거 (백트래킹: 상태 원상복구)

# 처음에는 아무것도 안 골랐으니 level=0, start=1부터 시작
dfs(0, 1)

