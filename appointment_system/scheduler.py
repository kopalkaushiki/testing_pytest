from utils import parse_time, is_overlap
from models import Appointment

class Scheduler:
    def __init__(self):
        self.appointments = []

    def is_available(self, start_time, end_time):
        for appt in self.appointments:
            if is_overlap(start_time, end_time, appt.start_time, appt.end_time):
                return False
        return True

    def book_appointment(self, start_str, end_str, user):
        start_time = parse_time(start_str)
        end_time = parse_time(end_str)

        if start_time >= end_time:
            raise ValueError("Invalid time range")

        if not self.is_available(start_time, end_time):
            raise Exception("Time slot already booked!")

        new_appt = Appointment(start_time, end_time, user)
        self.appointments.append(new_appt)
        return new_appt