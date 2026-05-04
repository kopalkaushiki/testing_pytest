import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from scheduler import Scheduler

def test_successful_booking():
    s = Scheduler()
    appt = s.book_appointment("09:00", "10:00", "User1")
    assert appt is not None

def test_overlap_booking():
    s = Scheduler()
    s.book_appointment("09:00", "10:00", "User1")

    with pytest.raises(Exception):
        s.book_appointment("9:30", "10:30", "User2")

def test_no_overlap():
    s = Scheduler()
    s.book_appointment("09:00", "10:00", "User1")
    appt = s.book_appointment("10:00", "11:00", "User2")

    assert appt is not None

def test_invalid_time():
    s = Scheduler()

    with pytest.raises(ValueError):
        s.book_appointment("11:00", "10:00", "User1")

def test_boundary_no_overlap():
    s = Scheduler()
    s.book_appointment("10:00", "11:00", "User1")

    # Starts exactly when previous ends → valid
    appt = s.book_appointment("11:00", "12:00", "User2")

    assert appt is not None

def test_exact_same_time_overlap():
    s = Scheduler()
    s.book_appointment("10:00", "11:00", "User1")

    with pytest.raises(Exception):
        s.book_appointment("10:00", "11:00", "User2")

def test_exact_same_time_overlap():
    s = Scheduler()
    s.book_appointment("10:00", "11:00", "User1")

    with pytest.raises(Exception):
        s.book_appointment("10:00", "11:00", "User2")

def test_inner_overlap():
    s = Scheduler()
    s.book_appointment("10:00", "12:00", "User1")

    # Completely inside existing slot
    with pytest.raises(Exception):
        s.book_appointment("10:30", "11:30", "User2")

def test_invalid_time_format():
    s = Scheduler()

    with pytest.raises(ValueError):
        s.book_appointment("abc", "11:00", "User1")

def test_zero_duration():
    s = Scheduler()

    with pytest.raises(ValueError):
        s.book_appointment("10:00", "10:00", "User1")