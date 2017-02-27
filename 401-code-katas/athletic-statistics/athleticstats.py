"""Solution for the athletic statistics Kata. https://www.codewars.com/kata/statistics-for-an-athletic-association"""
"""
OUTPUT FORMAT: "Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"
"""


def stat(strg):
    """Given an input string of race times, return mean, median, mode for race times."""
    race_times = strg.split(",")
    for idx, time in enumerate(race_times):
        race_times[idx] = convert_time_str_to_seconds(time)
    race_range = convert_sec_to_time_str(calculate_range(race_times))
    mean = convert_sec_to_time_str(calculate_mean(race_times))
    median = convert_sec_to_time_str(calculate_median(race_times))
    return "Range: {0} Average: {1} Median: {2}".format(race_range, mean, median)


def convert_time_str_to_seconds(time_str):
    """Given a string format, convert it to integer seconds."""
    time = time_str.split("|")
    time = [item if item else '00' for item in time]
    sec = 0
    sec += int(time[0]) * 3600      # Convert hours to seconds.
    sec += int(time[1]) * 60        # Convert minutes to seconds.
    sec += int(time[2])             # Add seconds.
    return sec


def convert_sec_to_time_str(total_seconds):
    """Given integer seconds, conver it to a time string."""
    hours = total_seconds // 3600
    minutes = total_seconds // 60 - 60 * hours
    seconds = total_seconds - 60 * minutes - 3600 * hours
    return "{0:02d}|{1:02d}|{2:02d}".format(int(hours), int(minutes), int(seconds))


def calculate_mean(times):
    """Given a list of times, calculate the mean."""
    return sum(times) / len(times)


def calculate_range(times):
    """Given a list of times, calculate the range."""
    return max(times) - min(times)


def calculate_median(times):
    """Given a list of times, calculate the median."""
    times.sort()
    if len(times) % 2:                  # Odd case
        return times[len(times) // 2]
    else:                               # Even case
        return calculate_mean([times[len(times) // 2], times[len(times) // 2 - 1]])
