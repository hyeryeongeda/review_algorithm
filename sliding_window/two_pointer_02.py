n, target = map(int, input().split())
arr = list(map(int, input().split()))
cnt, sum_v = 0, 0
right, left = 0, 0 # left right 모두 0에서 시작

while True:
    # 합이 타겟 이상이거나 right가 끝에 도달했을때 -> 범위 좁히기
    if sum_v >= target or right == n:
        sum_v -= arr[left] # left 값을 빼고
        left += 1 # left를 오른쪽으로 이동 (범위 좁히기)

    elif sum_v < target:
        sum_v += arr[right] # right 값을 더하고
        right += 1 # right를 오른쪽으로 이동 (범위 넓히기)

    if sum_v == target: cnt += 1

    # 왼쪽 포인터가 n에 도달하면 break
    if left == n: break

print(cnt)