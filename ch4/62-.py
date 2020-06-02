data = [1, 3, 5, 7, 9]  # 清單中裝著一些整數
# 請開始寫"寫入檔案"的程式碼
# print(len(data))

with open('test.txt', 'w') as f:
    for i in data:
        i = str(i)
        f.write(i + '\n')
