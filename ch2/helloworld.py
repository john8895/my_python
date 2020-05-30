# print("hello world")

# 註解
# 代碼風格 PEP8
# 代碼註釋

# a = ['aaa','bbb']
#
# a.append('ccc')
# print(a)

# for car in a:
#     print(car)

# students = ['Allen', 'Tom', 'Mayday', 'JJ', 'Jolin', 'Jay', 'Jam']
# for student in students:
#     print('Hi', student)

# cars = 'Audi'
# for car in cars:
#     print(car)
# print('cars length',len(cars))
# print('Au' in cars)
# print('B' in cars)

# data = []
# with open('food.txt', 'r') as f:
#     for line in f:
#         data.append(line.strip())
# print(data)

data = []
count = 0
with open('original.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了，共有', len(data), '筆資料')

sum_len = 0
for d in data:
    sum_len += len(d)
print('留言的平均長度為', sum_len / len(data), '個字')

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '筆留言長度小於100')
print(new[0])
print(new[1])

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('一共有',len(good),'筆留言提到good')
print(good[0])


good2 = [1 for d in data if 'good' in d]
print(len(good2))
print(good2[0])


bad = ['bad' in d for d in data]
print(bad)
