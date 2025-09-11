chars = ['A', 'B']
res = []
for a in chars:
    for b in chars:
        res.append(a + b)
print(res)  # ['AA','AB','BA','BB']