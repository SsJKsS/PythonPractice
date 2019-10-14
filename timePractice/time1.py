#如何判斷某⼀一個⽇日期是否存在？e.g.2000/2/29
pingnianMonth = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #平年月份天數
runnianMonth = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  #閏年月份天數 2月有29天


date = input("輸入日期:").split('/')
year = int(date[0])  # 截取年份
month = int(date[1])  # 截取月份
day = int(date[2])  # 截取日期
isRunNian = False

if month < 1 or month > 12:  # 判斷月份是否合法
    print('不存在')
    exit()

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
# 1. 西元年份除以4可整除，且除以100不可整除，為閏年。
# 2. 西元年份除以400可整除，為閏年。
    isRunNian = True

if isRunNian == False:
        if day < 1 or day > pingnianMonth[month]:  # 判斷日期是否合法
            print('不存在')
        else:
            print('有效日期')
else:
    if day < 1 or day > runnianMonth[month]:  # 判斷日期是否合法
        print('不存在')
    else:
        print('有效日期')
