from datetime import datetime

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M")

def is_overlap(start1, end1, start2, end2):
    return start1 < end2 and start2 < end1