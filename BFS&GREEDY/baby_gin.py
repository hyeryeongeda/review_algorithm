path = []
used = [0] * 6
baby_gin_result = False

def is_baby_gin():
    cnt = 0
    a, b, c = sorted([path[0], path[1], path[2]])
    if a == b == c:
        cnt += 1
    elif a+1 == b and b+1 == c:
        cnt += 1

    a, b, c = sorted([path[3], path[4], path[5]])
    if a == b == c:
        cnt += 1
    elif a+1 == b and b+1 == c:
        cnt += 1

    return cnt == 2


def recur(cnt):
    global baby_gin_result
    if cnt == 6:
        if is_baby_gin():
            baby_gin_result = True
        return

    for idx in range(6):
        if used[idx]:
            continue

        used[idx] = 1
        path.append(arr[idx])
        recur(cnt + 1)
        path.pop()
        used[idx] = 0

arr = list(map(int, input().split()))
recur(0)

print('Yes') if baby_gin_result else print('No')