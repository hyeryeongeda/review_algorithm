# 입력: 6장의 숫자 카드 (예: 1 2 3 3 2 1)
arr = list(map(int, input().split()))

used = [0] * 6     # used[i] : arr[i] 카드를 path에 썼는가? (중복 방지용)
path = []          # 지금까지 뽑은 6장의 "순서"를 담는 배열 (순열 생성)
is_babygin = 0     # 정답 플래그 (1이면 베이비진 발견)

def is_triplet(triple):
    # 같은 숫자 3장
    return triple[0] == triple[1] == triple[2]

def is_run(triple):
    # 연속 3장: 순서가 섞일 수 있으니 "정렬 후" 연속성 검사
    t = sorted(triple)
    return (t[0] + 1 == t[1]) and (t[1] + 1 == t[2])

def is_baby_gin_now():
    """
    path[0:3], path[3:6] 을 각각 run 또는 triplet인지 검사
    둘 다 만족(cnt==2)이면 베이비진
    """
    a, b = path[:3], path[3:]
    cnt = 0
    if is_triplet(a) or is_run(a):
        cnt += 1
    if is_triplet(b) or is_run(b):
        cnt += 1
    return cnt == 2

def recur(lev):
    """
    lev(레벨) : 현재까지 선택한 카드 수 (0 ~ 6)
    branch   : 이 레벨에서 '아직 쓰지 않은 카드 인덱스들' (0~5 중 used[i]==0)
    used     : 중복 없는 '순열'을 만들기 위한 체크 배열
    """
    global is_babygin

    # 이미 정답을 찾았으면 더 탐색할 필요 없음 (조기 종료 가지치기)
    if is_babygin:
        return

    # 6장 모두 뽑았으면 베이비진 판정
    if lev == 6:
        if is_baby_gin_now():
            is_babygin = 1
        return

    # branch: 6개 카드 중 아직 안 쓴 카드 하나를 뽑아 다음 레벨로
    for i in range(6):
        if used[i]:                # 이미 path에 쓴 카드면 패스 (중복 방지)
            continue
        used[i] = 1                # i번째 카드 사용 체크
        path.append(arr[i])        # 순열에 현재 카드 추가
        recur(lev + 1)             # 다음 레벨(다음 카드 선택)로 진입
        path.pop()                 # 백트래킹: 상태 복구
        used[i] = 0                # 사용 체크 해제

# 탐색 시작 (level=0부터 6장의 순열 만들기)
recur(0)

print('Yes' if is_babygin else 'No')
