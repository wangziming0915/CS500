print("This program finds the time x minutes before and after input time")

timeList = input("Enter a time (hh:mm): ").split(':')
hours = int(timeList[0])
minute = int(timeList[1])
shift = int(input("Enter a time shift in mins: "))

totalMins = hours * 60 + minute

totalMinsBefore = totalMins - shift
hoursBefore = (totalMinsBefore // 60) % 24
minuteBefore = totalMinsBefore % 60

totalMinsAfter = totalMins + shift
hoursAfter = (totalMinsAfter // 60) % 24
minuteAfter = totalMinsAfter % 60


print("Before: {0:02d}:{1:02d}".format(hoursBefore, minuteBefore))
print("After: {0:02d}:{1:02d}".format(hoursAfter,minuteAfter))

