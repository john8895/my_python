password = 'a123456'
chance = 3
while chance > 0:
    chance = chance - 1
    login = input('請輸入密碼: ')
    if login == password:
        print('登入成功')
        break
    else:
        print('密碼錯誤')
        if chance > 0:
            print('還有', chance, '次機會')
