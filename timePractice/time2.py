#印出: “西元2017年03月08日 PM 11:30:42”
import time

#用時間元祖time.struct_time裡的內建時間變數去做判斷
#time.struct_time(tm_year=2019, tm_mon=10, tm_mday=14, tm_hour=14, tm_min=23, tm_sec=13, tm_wday=0, tm_yday=287, tm_isdst=0)
tm_year = time.localtime().tm_year
tm_mon = time.localtime().tm_mon
tm_mday = time.localtime().tm_mday
tm_hour = time.localtime().tm_hour
tm_min = time.localtime().tm_min
tm_sec = time.localtime().tm_sec
if tm_hour >= 12 and tm_sec >= 0:  # 取小時和秒數判斷AM或PM
    print('西元',tm_year,'年',tm_mon,'⽉',tm_mday,'⽇ ' 'PM',tm_hour,':',tm_min,':',tm_sec)
else:
    print('西元',tm_year,'年',tm_mon,'⽉',tm_mday,'⽇ ' 'AM',tm_hour,':',tm_min,':',tm_sec)











