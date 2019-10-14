#今天是今年的第N天
import time

#用時間元祖time.struct_time裡的內建時間變數去做判斷
#time.struct_time(tm_year=2019, tm_mon=10, tm_mday=14, tm_hour=14, tm_min=23, tm_sec=13, tm_wday=0, tm_yday=287, tm_isdst=0)
tm_yday = time.localtime().tm_yday
print('今天是今年的第',tm_yday,'天')






















