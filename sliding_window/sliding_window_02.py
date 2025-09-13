# 배열에서 길이 5짜리 연속 부분합 중 가장 큰 합의 시작 인덱스를 구하는 알고리즘.
arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]

N = len(arr)
M = 5

def get_sum(idx):
    sum_v = 0
    # 5개의 합
    for i in range(5):
        sum_v += arr[idx + i] # +0, +1, +2, +3, +4 인덱싱  
    return sum_v

max_v = float('-inf')   # 아주 작은 값으로 초기화 (음의 무한대)
for idx in range(N-M+1):  # 0부터 6까지 (11-5+1=7개 위치)
    ret = get_sum(idx)    # 해당 위치에서 5개 합
    if ret > max_v:       # 더 크면 갱신
        max_v = ret
        max_idx = idx     # 최대합의 시작 인덱스 기록


print(max_idx)
        