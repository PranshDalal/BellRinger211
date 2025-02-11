from datetime import datetime, time

now = datetime.now()
print(now)
specific_time = time(14, 19, 0) 

now_time = now.time()
time_difference = datetime.combine(now.date(), specific_time) - datetime.combine(now.date(), now_time)
print(time_difference)
