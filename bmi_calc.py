cm = float(input('請輸入身高:'))
kg = float(input('請輸入體重:'))
bmi = kg / (cm / 100) ** 2
print('你的BMI是:', round(bmi, 0))
