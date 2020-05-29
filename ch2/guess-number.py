import random

r = random.randint(1, 100)
count = 0
while True:
    count += 1
    num = input('請輸入 1-100 的一個數字:')
    num = int(num)
    if num > 100 or num < 1:
        print('輸入錯誤！')
        break
    if num == r:
        print('猜', count, '次猜對了！遊戲結束')
        break
    elif num > r:
        print('比答案大')
    elif num < r:
        print('比答案小')
    print('你猜第', count, '次')
