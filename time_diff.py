#first time input
print("******Enter the start time********")
th1 = int(input("Enter the time in hours :"))
tm1 = int(input("Enter the time in minute :"))
ts1 = int(input("Enter the time in second :"))

#second time input
print("******Enter the end time********")
th2 = int(input("Enter the time in hours :"))
tm2 = int(input("Enter the time in minute :"))
ts2 = int(input("Enter the time in second :"))


# Main logic for calculating the difference
# This is used to calculate the second
if(ts2 > ts1):
    tm1 = tm1-1
    ts1 = ts1+60
else:
    ress = ts1 - ts2
# this is used to calculate the minute
if(tm2 > tm1):
    th1 = th1-1
    tm1 = tm1+60
else:
    resm = tm1-tm2
# this will used to calculate the hours 
    # our 75% work is done in upper two logic so we have to directly calculate hours 
resh = th1-th2

print("Time difference is",resh,":",resm,":",ress)
