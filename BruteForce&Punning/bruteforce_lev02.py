#완전탐색 (모든 쌍 확인)
arr = [1, 2, 3, 4, 5]
T = 6

pairs = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == T:
            pairs.append((arr[i], arr[j]))
print(pairs)  # [(1,5), (2,4)]