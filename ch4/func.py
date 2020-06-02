# def wash(dry=False, water=8):
#     print('加水', water, '分滿')
#     print('加洗衣精')
#     print('旋轉')
#     if dry:
#         print(dry, '烘衣服')
#
#
# wash(True, 10)
#
#
# def say_hi():
#     print('hi!')
#
#
# say_hi()
#
#
# def add(x=0, y=0):
#     print(x + y)
#
#
# add(123, 1223)
#
#
# add()


# def average(numbers):
#     avg = sum(numbers) / len(numbers)
#     return avg
#
#
# print(average([1, 2, 3]))
# print(average([1, 2, 3]))

# 測驗

# def add(x, y):
#     print(x + y)
#
#
# add(1, 1)

# def hello(x, y=1):
#     print(x, y)
#
#
# hello(3, 4)

def crazy(x, y=3, z=2):
    return x * 2 + y * 3 + z


crazy(2)  # 15
crazy(3, 1)  # 11
crazy(3, 2, 0)  # 12

# 以上沒有print或接收值，所以不會印出東西
