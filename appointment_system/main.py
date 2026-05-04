from scheduler import Scheduler

scheduler = Scheduler()

# Example usage
try:
    scheduler.book_appointment("10:00", "11:00", "Alice")
    scheduler.book_appointment("11:00", "12:00", "Bob")

    # This should fail (overlap)
    scheduler.book_appointment("10:30", "11:30", "Charlie")

except Exception as e:
    print(e)

for appt in scheduler.appointments:
    print(appt)