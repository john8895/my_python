import os


# 讀取檔案
def read_file(filename):
    products = []
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            if '商品,價格' in line:  # 略過標題
                continue
            name, price = line.strip().split(',')
            print(name, price)
            products.append([name, price])
    print(products)
    return products


# 讓使用者輸入
def user_input(products):
    while True:
        name = input('請輸入商品名稱:')
        if name == 'q':
            break
        price = input('請輸入商品價格:')
        products.append([name, price])
    print(products)
    return products


# 把商品與價格印出來
def print_products(products):
    for p in products:
        print(p[0], '的價格是', p[1])


# 寫入檔案
def save_file(filename, products):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('商品,價格\n')
        for p in products:
            f.write(p[0] + ',' + p[1] + '\n')


def main():
    filename = 'products.csv'
    if os.path.isfile(filename):  # 檢查檔案在不在？
        print('yeah! 找到檔案了！')
    else:
        print('檔案不存在！')
        return False
    products = read_file(filename)
    user_input(products)
    print_products(products)
    save_file(filename, products)


main()
