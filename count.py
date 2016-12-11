from __future__ import division
from entropy import entropy


class Count:
    def __init__(self, yes, no):
        self.yes = yes
        self.no = no

    def addYes(self):
        self.yes = self.yes + 1

    def addNo(self):
        self.no = self.no + 1

    def totalYesAndNo(self):
        return self.yes + self.no

    def calculateEntropy(self):
        return entropy(self.yes / self.totalYesAndNo())
