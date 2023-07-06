class Date:
    def __init__(self,
                 day: int,
                 month: int,
                 year: int):
        """
            Gün, Ay, Yıl şeklinde tam sayı girdileri almaktadır.
        """
        self.day = day
        self.month = month
        self.year = year
    def __gt__(self, other):
        if self.year > other.year:
            return True
        elif self.year == other.year and self.month > other.month:
            return True
        elif self.year == other.year and self.month == other.month and self.day > other.day:
            return True
        return False
    def __eq__(self, __value: object) -> bool:
        if self.year == __value.year and self.month == __value.month and self.day == __value.day:
            return True
        return False
    def __str__(self):
        return str(self.day) + "/" + str(self.month) + "/" + str(self.year)