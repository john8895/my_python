# 99乘法表

# 用for迴圈
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(i, 'x', j, '=', i * j)
#     print('')

# 用while迴圈
i = 1
while i < 10:
    j = 1
    while j < 10:
        s = i * j
        print(i, 'x', j, '=', s)
        j += 1
    print('')
    i += 1
