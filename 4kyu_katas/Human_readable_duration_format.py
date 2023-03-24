'''
Your task in order to complete this Kata is to write a function which formats a duration,
given as a number of seconds, in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc.
In general, a positive integer and one of the valid units of time, separated by a space.
The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", ").
Except the last component, which is separated by " and ", just like it would be written in English.

A more significant units of time will occur before than a least significant one.
Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero.
, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible".
It means that the function should not return 61 seconds, but 1 minute and 1 second instead.
Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
'''

def format_duration(seconds):
    if seconds == 0:
        return 'now'
    result = ''

    years = seconds // (60 * 60 * 24 * 365)
    if years >= 1:
        result = str(years) + ' year'
        if years > 1:
            result += 's'

    seconds = seconds - years * (60 * 60 * 24 * 365)
    days = seconds // (60 * 60 * 24)
    if years != 0 and seconds != 0:
        result += ', '
    if days >= 1:
        result = result + str(days) + ' day'
        if days > 1:
            result += 's'

    seconds = seconds - days * (60 * 60 * 24)
    hours = seconds // (60 * 60)
    if days != 0 and seconds != 0:
        result += ', '
    if hours >= 1:
        result = result + str(hours) + ' hour'
        if hours > 1:
            result += 's'

    seconds = seconds - hours * (60 * 60)
    minute = seconds // 60
    if hours != 0 and seconds != 0:
        result += ', '
    if minute >= 1:
        result = result + str(minute) + ' minute'
        if minute > 1:
            result += 's'

    seconds = seconds - minute * 60
    if minute != 0 and seconds != 0:
        result += ', '
    if seconds >= 1:
        result = result + str(seconds) + ' second'
        if seconds > 1:
            result += 's'

    if result.count(',') == 1:
        result = result.replace(', ', ' and ')
    if result.count(',') > 1:
        result = result[:result.rfind(',')] + ' and' + result[result.rfind(',')+1:]

    return result


assert format_duration(1) == "1 second"
assert format_duration(62) == "1 minute and 2 seconds"
assert format_duration(120) == "2 minutes"
assert format_duration(3600) == "1 hour"
assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"

