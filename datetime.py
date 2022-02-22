'''
This program chekcs logs over time. It returns the point(s) in time when a system has too much errors
in a specified time interval. The parameters are specifies before the logs starts. The first number describes 
a time interval. The second number describes the amout of errors inside this time interval which is not acceptable. 
In the following example 2 errors in an interval of 2 second is too much. 
The output of the progam is "[2020-03-17 00:01:10] ERROR Cant write varlogyes1"
2 2
[2020-03-16 23:59:59] ERROR Disk crash
[2020-03-17 00:00:01] SOMETHING Network failute
[2020-03-17 00:00:01] SOMETHING Network failute
[2020-03-17 00:00:02] SOMETHING Cant write varlogyes
[2020-03-17 00:00:02] SOMETHING Cant write varlogyes
[2020-03-17 00:00:03] SOMETHING Network failute
[2020-03-17 00:00:03] ERROR Cant write varlog
[2020-03-17 00:00:04] SOMETHING Network failute
[2020-03-17 00:00:04] SOMETHING Cant write varlogyes
[2020-03-17 00:00:05] ERROR Cant write varlogyes
[2020-03-17 00:00:07] SOMETHING Network failute
[2020-03-17 00:00:08] SOMETHING Network failute
[2020-03-17 00:01:08] SOMETHING Network failute
[2020-03-17 00:01:09] ERROR Cant write varlogyes
[2020-03-17 00:01:10] ERROR Cant write varlogyes
'''

from datetime import datetime

the_file          = open('input.txt')
time_par, err_par = map(int, the_file.readline().split())
messages          = the_file.readlines()

#This list will contain the time of relevant errors
err_time = []

for message in messages: 
        
    cur_time, cur_log = message.split(']')

    #If the message is not an error we ignore it 
    if 'ERROR' not in cur_log: continue

    #Add the time of the newest error
    err_time.append(datetime.strptime(cur_time[1:], '%Y-%m-%d %H:%M:%S'))
    
    #Checking how much errors we observed
    if len(err_time) >= err_par:

        #Checking time difference from last observed to first observed error
        time_to_first = (err_time[-1] - err_time[0]).total_seconds()

        #If the time from the last to first is too small the program stops
        if time_to_first < time_par:
            print(message)
            break
        
        #else the program deletes the first observed error - out of the time interval
        err_time.pop(0)
