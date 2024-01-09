from datetime import datetime, timedelta


def parse_time(time_str):
    return datetime.strptime(time_str, '%H:%M')


busy = [
    {'start': '10:30', 'stop': '10:50'},
    {'start': '18:40', 'stop': '18:50'},
    {'start': '14:40', 'stop': '15:50'},
    {'start': '16:40', 'stop': '17:20'},
    {'start': '20:05', 'stop': '20:20'}
]

start_time = parse_time('9:00')
end_time = parse_time('21:00')
curr_time = start_time
window = timedelta(minutes=30)

sorted_busy = sorted(busy, key=lambda x: x['start'])
free_intervals = []
i = 0

while curr_time <= end_time - window:
    if i < len(sorted_busy):
        start = parse_time(sorted_busy[i]['start'])
        stop = parse_time(sorted_busy[i]['stop'])
    else:
        start = stop = end_time
    while curr_time <= start - window:
        free_intervals.append([curr_time, curr_time + window])
        curr_time += window
    curr_time = stop
    i += 1

for i in free_intervals:
    print(f'{i[0].strftime("%H:%M")} - {i[1].strftime("%H:%M")}')
