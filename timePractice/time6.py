#2010~2020年間母親節的日期(五月第二個星期日)

# 母親節的日期(五月第二個星期日)
# 5/1是星期一 +13天 = 第二個星期天
# 5/1是星期二 +12天 = 第二個星期天
# 5/1是星期三 +11天 = 第二個星期天
# 5/1是星期四 +10天 = 第二個星期天
# 5/1是星期五 +9天 = 第二個星期天
# 5/1是星期六 +8天 = 第二個星期天
# 5/1是星期天 +7天 = 第二個星期天
import time

dayList = [13,12,11,10,9,8,7]  # 先宣告一個列表把需加的天數依照星期一~星期日塞進去
for i in range(2010,2021):
    tupleFormat = (i,5,1,0,0,0,0,0,0)
# 用時間元組time.struct_time裡的內建時間變數去做判斷
# 時間元組內有(tm_year, tm_mon, tm_mday, tm_hour, tm_min, tm_sec, tm_wday, tm_yday, tm_isdst)共9個變數
# 宣告一個元組變數，然後把已知條件tm_year, tm_mon, tm_mday先丟值進去，未知的都塞0，等等要藉由mktime()來轉為時間數值
    dateTransform = time.mktime(tupleFormat)
# 宣告一個變數儲存轉變完成的時間數值
    motherDay = dayList[time.localtime(dateTransform).tm_wday] + 1
    print("%s-5-%s" %(i, motherDay))

