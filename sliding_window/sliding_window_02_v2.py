arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]
N = len(arr)
M = 5

# 1) 첫 창문 합 (idx = 0 ~ M-1)
window = sum(arr[:M])
max_sum = window
max_idx = 0  # 최댓값 시작 인덱스 (동률이면 가장 앞 인덱스 유지)

# 2) 창문을 오른쪽으로 한 칸씩 밀기
#    새로 들어오는 값: arr[i + M - 1]
#    빠져나가는 값:   arr[i - 1]
for i in range(1, N - M + 1):
    window += arr[i + M - 1] - arr[i - 1]
    if window > max_sum:
        max_sum = window
        max_idx = i

print(max_idx)   # 최대 합을 만드는 시작 인덱스
print(max_sum) # (원하면 최대 합도 출력)
