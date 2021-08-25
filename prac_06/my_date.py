"""
Describe a date
"""
MONTH_29 = (2,)
MONTH_30 = (4, 6, 9, 11)
MONTH_31 = (1, 3, 5, 7, 8, 10, 12)


def get_max_day(month: int, year: int):
    if month in MONTH_29:
        max_day = 29 if year % 4 == 0 else 28
    elif month in MONTH_30:
        max_day = 30
    else:
        max_day = 31
    return max_day


class MyDate:
    """Describe a date"""

    def __init__(self, day: int, month: int, year: int):
        """Constructor"""
        self.year = year if year >= 1 else 1

        if month < 1:
            self.month = 1
        elif month > 12:
            self.month = 12
        else:
            self.month = month

        max_day = get_max_day(self.month, self.year)
        if day < 1:
            self.day = 1
        elif day > max_day:
            self.day = max_day
        else:
            self.day = day

    def __str__(self):
        """Description of the class"""
        return "{0:>2}-{1:>2}-{2}".format(str(self.day).zfill(2), str(self.month).zfill(2), self.year)

    def add_day(self, day: int):
        if day <= 0:
            return

        # Placeholder of date
        current_day = self.day
        current_month = self.month
        current_year = self.year

        # Add an extra day since date can't start from 0
        day += 1
        while day > 0:
            max_day = get_max_day(current_month, current_year)
            day_difference = max_day - current_day + 1
            if day - day_difference <= 0:
                current_day += day - 1
                day = 0
            else:
                current_day = 1
                current_month += 1
                if current_month > 12:
                    current_month = 1
                    current_year += 1
                day -= day_difference

        self.day = current_day
        self.month = current_month
        self.year = current_year



