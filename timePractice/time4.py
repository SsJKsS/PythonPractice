#昨天是星期幾
import time

#用時間元祖time.struct_time裡的內建時間變數去做判斷
#time.struct_time(tm_year=2019, tm_mon=10, tm_mday=14, tm_hour=14, tm_min=23, tm_sec=13, tm_wday=0, tm_yday=287, tm_isdst=0)
tm_wday = time.localtime().tm_wday # tm_wday變數從0~6 -> 星期一~星期天
weekday = ['一','二','三','四','五','六','天']  # 宣告一個星期列表方便等等印出
print('昨天是星期',weekday[tm_wday-1])


















