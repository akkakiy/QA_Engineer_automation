times = '1h 45m,360s,25m,30m 120s,2h 60s'
time_str = []
for time in (times.split(',')):
    moments = time.split()
    res = 0
    for moment in moments:
        if 'h' in moment:
            res += int(moment.replace('h','')) * 60
        if 'm' in moment:
            res += int(moment.replace('m', ''))
        if 's' in moment:
            res += int(moment.replace('s','')) // 60
    time_str.append(res)
total = sum(time_str)
print('Сумма минут:', total)