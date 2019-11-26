class LeapYear:
    def __init__(self, year):
        self.year = year

    def answer(self):
        year = self.year
        if year % 100 == 0:
            if year % 400 == 0:
                return "%d 是闰年" % year
            else:
                return "%d 不是闰年" % year
        else:
            if year % 4 == 0:
                return "%d 是闰年" % year
            else:
                return "%d 不是闰年" % year
