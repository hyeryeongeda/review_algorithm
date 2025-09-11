arr = [1, 3, 7, 9, 11]
target = 9

found = False
for x in arr:              # 모든 원소를 '전부' 확인
    if x == target:
        found = True
        break
print(found)  # True