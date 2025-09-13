arr = [4, 5, 1, 1, 5, 4, -3, -13, 9, 20, 13]

# 처음 윈도우 계산
sum_v = sum(arr[:5]) # 슬라이싱
max_v = sum_v
max_idx = 0

# N-M
for i in range(len(arr)-5):
    # 1. 다음 윈도우 계산 (현재 i를 기준으로 다음 윈도우를 계산)
    sum_v -= arr[i] # 첫번째 element 제거
    sum_v += arr[i + 5] # 마지막 element 추가

    # 2. 최대값 갱신
    if sum_v > max_v:
        max_v = sum_v # 다음 윈도우의 합
        # 현재 윈도우의 index는 : i, 다음 윈도우의 index : i + 1
        max_idx = i + 1

print(max_idx)