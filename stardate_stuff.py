from math import floor
from dateutil.parser import parse
from datetime import datetime
from argparse import ArgumentParser
from time import mktime


class StarDate():
    date = None
    stardate = None

    def __init__(self, date=None):
        self.date = date

    def setDate(self, date):
        self.date = date

    def to_seconds(self, date):
        return mktime(date.timetuple())

    def getStardate(self):
        if(self.date != None):
            stardateRequested = parse(self.date)
        else:
            stardateRequested = datetime.now()

        stardateOrigin = parse("1987-07-15T00:00:00-00:00")

        self.stardate = self.to_seconds(stardateRequested) - self.to_seconds(stardateOrigin)
        self.stardate = self.stardate / (60.0 * 60.0 * 24.0 * 0.036525)
        self.stardate = floor(self.stardate + 410000.0)
        self.stardate = self.stardate / 10.0

        return self.stardate


            