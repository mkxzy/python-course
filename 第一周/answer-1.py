time_minute = 43.5
time_hour = 43.5 / 60
distance_km = 10
distance_mile = 10 / 1.61

time_for_one_mile = time_hour / distance_mile
print("每英里花费时间：%.4f小时" % time_for_one_mile)

speed_mile = 1 / time_for_one_mile
print("平均速度是：%.4f英里/小时" % speed_mile)
