# Name: Baaba
# Partners name: Diego
# Rating: 5
# Time taken:
# Comment: It was stressful for the last bits but overall cool

import pytest
import time_of_day


def test_time_of_day_morning():
        # Testing for the time of morning with the number 9 because it takes less than 0 or greater than 2400
    assert time_of_day.what_time_of_day(9) == "Morning"


def test_time_of_day_afternoon():
        # Testing for the time of afternoon with the number of 1500 because the number is between 1200 and 1759
    assert time_of_day.what_time_of_day(1500) == "Afternoon"


def test_evening():
    # Testing for the time of evening with the number of 2000 because the number is between 1800 and 2059
    assert time_of_day.what_time_of_day(2000) == "Evening"

def test_late_night():
        # Testing for the time of late night using 2100 because is in between 2059 and 2400
    assert time_of_day.what_time_of_day(2100) == "Late Night"