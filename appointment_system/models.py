class Appointment:
    def __init__(self, start_time, end_time, user):
        self.start_time = start_time
        self.end_time = end_time
        self.user = user

    def __repr__(self):
        return f"{self.user}: {self.start_time} - {self.end_time}"
