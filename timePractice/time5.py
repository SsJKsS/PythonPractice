#2010年10月10日與2017年2月2日相差幾日
import datetime

date2017 = datetime.date(2017,2,2)  # 設定要相減的日期
date2010 = datetime.date(2010,10,10)  # 設定要相減的日期
result = date2017 - date2010
print(result.days)  # 相差的天數

#=====================================================================================
#今天和2010年10月10日相差幾日
print('=====延伸練習=====')
today = datetime.date.today()  # 抓取今天日期
result = today - date2010
print(result.days)







