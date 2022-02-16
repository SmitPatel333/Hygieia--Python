from Leveling import *

class Character:
    level_system = Leveling_System(None, None)
    days = 1
    time_eaten = []
    total_calories = 0
    

    def __init__(self, level, days):
        self.level_system = level
        self.days = days

    def getday(self):
        return self.days
    
    def update_time_eaten(self, time):
        self.time_eaten.append(time)

    def update_total_calories(self, calories):
        self.total_calories = calories

    def end_of_day(self):
        self.level_system.give_points(self.time_eaten, self.total_calories)
        self.level_system.level_up()

        print("Day:", self.days)
        print("Points:", self.level_system.getpoints())
        print("Level:", self.level_system.getlevel())

        self.time_eaten = []
        self.total_calories = 0
        self.days += 1