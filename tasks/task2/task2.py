import sys
print("log file analysis")
print("=================\n")
log = sys.argv[1]

def file_list(log):
    with open(log, 'r') as file:
        line=[lines.strip().split(',')for lines in file]
    return line

def mycat(data):
    tdifference = [ ]
    arrived = 0
    left = 0
    my_cat = 0
    intruder_attacks = 0
    for i in data:
        if i[0] == "OURS":
            my_cat += 1
            arrived = int(i[1])
            left = int(i[2])
            tdifference.append(left - arrived)
        else:
            intruder_attacks += 1
    return my_cat, tdifference, intruder_attacks

def total_time(time_difference):
    time = 0
    for i in time_difference:
        time += i
    return time

def my_duration(time):
    hours = time // 60
    mins = time % 60
    return hours, mins

def maximum(time_difference):
    max_val = time_difference[0]
    for i in time_difference:
        if i > max_val:
            max_val = i
    return max_val

def minimum(time_difference):
    min_val = time_difference[0]
    for i in time_difference:
        if i < min_val:
            min_val = i
    return min_val

def average(mn, mx):
    avg = (mn + mx) / 2
    return int(avg)

def display(max_val, min_val, avg, my_cat, intruder_attacks, hours, mins):
    print(f"Cat Visits: {my_cat}")
    print(f"Other Cats: {intruder_attacks}\n")
    if hours >1 and mins >1:
        print(f"Total time in house: {hours} Hours {mins} Minutes\n")
    elif hours >1 and mins<=1:
        print(f"Total time in house: {hours} Hours {mins} Minute\n")
    elif hours <=1 and mins>1:
        print(f"Total time in house: {hours} Hour {mins} Minutes\n")
    else:
        print(f"Total time in house: {hours} Hour {mins} Minute\n")
    print(f"Average Visit Length: {avg} Minutes")
    print(f"Longest Visit:        {max_val} Minutes")
    print(f"Shortest Visit:       {min_val} Minutes\n")

data = file_list(log)
my_cat, tdifference, intruder_attacks = mycat(data)
time=total_time(tdifference)
hours, mins = my_duration(time)
max_val=maximum(tdifference)
min_val=minimum(tdifference)
avg=average(min_val, max_val)
display(max_val, min_val, avg, my_cat, intruder_attacks, hours, mins)