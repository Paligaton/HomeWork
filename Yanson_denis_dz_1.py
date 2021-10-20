import re

class DateParse:

    def __init__(self, dd, mm, yy):
        self.day=dd
        self.month=mm
        self.year=yy

    @classmethod
    def parse(cls, txt):
        RE_LINE = re.compile(r'^(\S+){1}-(\S+){1}-(\S+){1}')
        cd = RE_LINE.findall(txt)
        cls.valid(cd)
        return cls(cd[0][0], cd[0][1], cd[0][2])

    @staticmethod
    def valid(txt):
        if len(txt) == 0:
            raise ValueError('wrong format')
        if not txt[0][0].isdigit() and  not txt[0][0].isdigit() and  not txt[0][0].isdigit():
            raise ValueError('wrong format date has a letter')
        if int(txt[0][0])>31 or int(txt[0][0])<1:
            raise ValueError('day bigger than 31 or less than 1')
        if int(txt[0][1])>12 or int(txt[0][1])<1:
            raise ValueError('month bigger then 12 or less than 1')



date = DateParse.parse('31-12-2000')
print(date.day.isdigit())