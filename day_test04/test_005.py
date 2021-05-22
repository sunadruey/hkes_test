import  time
# 获取2天前的时间
now_time=time.time()
two_day_before = now_time-60*60*24*2
time_tuple=time.localtime(two_day_before)
print(time.strftime("%Y年%m月%d日 %H:%M:%S", time_tuple))