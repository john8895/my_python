import os

products = []

if os.path.isfile('products.csv'): # 檢查檔案在不在？
    print('yeah! 找到檔案了！')
    with open('products.csv', 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line: # 略過標題
                continue
            name, price = line.strip().split(',')
            print(name, price)
            products.append([name, price])
else:
    print('檔案不存在！')


# 讀取檔案


print(products)

# 讓使用者輸入
while True:
    name = input('請輸入商品名稱:')
    if name == 'q':
        break
    price = input('請輸入商品價格:')
    products.append([name, price])
print(products)

# 把商品與價格印出來
for p in products:
    print(p[0], '的價格是', p[1])

# 寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
    f.write('商品,價格\n')
    for p in products:
        f.write(p[0] + ',' + p[1] + '\n')
