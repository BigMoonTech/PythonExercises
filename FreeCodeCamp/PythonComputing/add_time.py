
def main():
    print(add_time("11:43 PM", "24:20", "tueSday"))


def add_time(start_time, time_to_add, start_day=None):
    
    start_time = start_time.split()
    hours = int(start_time[0].split(':')[0])
    mins = int(start_time[0].split(':')[1])
    ampm = start_time[1].lower()
    time_to_add = time_to_add.split(':')
    sum_mins = (int(time_to_add[0]) * 60) + int(time_to_add[1])
    days_later = 0

    weekdays = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }

    weekdays_rev = {
        'monday': 0,
        'tuesday': 1,
        'wednesday': 2,
        'thursday': 3,
        'friday': 4,
        'saturday': 5,
        'sunday': 6
    }

    while sum_mins != 0:
        mins += 1

        # anytime the minutes moves to 60 reset minutes to zero and increment hours by 1
        if mins == 60:
            hours += 1
            mins = 0

            # anytime the hours moves to 12 we need to switch the am/pm sign
            if hours == 12:

                # flip am to pm and vice versa
                if ampm == 'am':
                    ampm = 'pm'
                else:
                    ampm = 'am'

                # when we switch to AM increment days_later by 1
                if ampm == 'am':
                    days_later += 1

            # when hours equals 13 we reset it back to 1
            if hours == 13:
                hours = 1

        sum_mins -= 1

    if start_day is not None:

        start_day = weekdays_rev[start_day.lower()]
        end_day = start_day + days_later

        if end_day > 6:
            end_day = end_day % 7

        # print statements if optional string given
        if days_later > 1:
            return f"{hours}:{mins:02d} {ampm.upper()}, {weekdays[end_day]} ({days_later} days later)"
        elif days_later == 1:
            return f"{hours}:{mins:02d} {ampm.upper()}, {weekdays[end_day]} (next day)"
        else:
            return f"{hours}:{mins:02d} {ampm.upper()}, {weekdays[end_day]}"

    else:
        # print statements if no optional string given
        if days_later > 1:
            return f"{hours}:{mins:02d} {ampm.upper()} ({days_later} days later)"
        elif days_later == 1:
            return f"{hours}:{mins:02d} {ampm.upper()} (next day)"
        else:
            return f"{hours}:{mins:02d} {ampm.upper()}"


if __name__ == '__main__':
    main()
