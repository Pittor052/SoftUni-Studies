exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())
time_of_exam = exam_hour * 60 + exam_minute
time_of_arrive = arrive_hour * 60 + arrive_minute
if time_of_arrive > time_of_exam:
    print("Late")
elif time_of_exam - 30 <= time_of_arrive <= time_of_arrive:
    print("On Time")
else:
    print("Early")
if time_of_exam - 60 < time_of_arrive < time_of_exam:
    difference = time_of_exam - time_of_arrive
    print(f"{difference} minutes before the start")
elif time_of_arrive <= time_of_exam - 60:
    difference = time_of_exam - time_of_arrive
    hours = difference // 60
    minutes = difference % 60
    print(f"{abs(hours)}:{abs(minutes):0>2d} hours before the start")
elif time_of_exam < time_of_arrive < time_of_exam + 60:
    difference = time_of_arrive - time_of_exam
    print(f"{difference} minutes after the start")
elif time_of_arrive >= time_of_exam + 60:
    difference = time_of_arrive - time_of_exam
    hours = difference // 60
    minutes = difference % 60
    print(f"{hours}:{minutes:0>2d} hours after the start")