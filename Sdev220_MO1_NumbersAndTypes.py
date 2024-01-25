## 3.1 How many seconds are in an hour? 
sec = 60 
min = (1 * sec)
hour = (min * 60)
print(str(min) + " seconds in one minute")

## 3.2 How many seconds are in a day, assigns a variave called "seconds_per_hour".
seconds_per_hour = hour
print(str( seconds_per_hour) + " seconds in one hour")

## 3.3 How many secons are in a day. assign a variable called " seconds_per_day".
seconds_per_day = (seconds_per_hour * 24)
## 3.4 calculate how many seconds per day, print variable "seconds_per_day".
print(str(seconds_per_day) + " seconds in one day")

##3.5 Divide seconds per day by seconds per hour. use a floating point.
hours_per_day = float(seconds_per_day / seconds_per_hour)
print(str( hours_per_day) + " hours per day")

##3.6 Divide seconds_per_day by seconds_per_hour using integer division
hours_per_day = int(seconds_per_day / seconds_per_hour)
print("there are " + str( hours_per_day) + " hours per day")
##Did this number agree with the floating-point value from the previous question, aside from the final .0?
print("the answer to the question is YES")

