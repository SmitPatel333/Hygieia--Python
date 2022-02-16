from math import *

class Leveling_System:
    #Variables for current points and levels, will be optimised later 
    points = 0
    level = 0

    #Temporary variables for recommended values
    recommended_times = []
    recommended_calories = None

    def __init__(self, times, calories):
        self.recommended_times = times
        self.recommended_calories = calories

    def getpoints(self):
        return self.points

    def getlevel(self):
        return self.level

    ''' 
        Function to give points as follows:
        Eating at the recommended times = 20 points per occurence (breakfast, lunch, dinner)
        Eating within the recomended calories count = 20 points
        Doing both in a day = bonus 40 points
    '''
    def give_points(self, eating_times, calories_consumed):
        global points
        global level

        if ((equals(eating_times, self.recommended_times)) and (calories_consumed in self.recommended_calories)):
            self.points += 120
        else:
            if(calories_consumed in self.recommended_calories):
                self.points += 20
        
            for i in range(len(eating_times)):
                time = eating_times[i]
                recommendation = self.recommended_times[i]
                if (time in recommendation):
                    self.points += 20
        
    '''
        Function to level up, it calculates the number of levels that you increase by 
        and subtracts the relevant number of points
        100 points/level until level 5
        200 points/level until level 15
        300 points/level until level 35
        500 points/level until level 50
    '''
    def level_up(self):
        if (self.level < 5):
            if (self.points >= 100):
                increase = floor(self.points/100)
                self.level += increase
                self.points -= increase*100

        elif (self.level < 15):
            if (self.points >= 200):
                increase = floor(self.points/200)
                self.level += increase
                self.points -= increase*200

        elif (self.level < 35):
            if (self.points >= 300):
                increase = floor(self.points/300)
                self.level += increase
                self.points -= increase*300

        else:
            if (self.points >= 500):
                increase = floor(self.points/500)
                self.level += increase
                self.points -= increase*500

def equals(list1, list2):
    counter = 0
    for i in range(len(list2)):
        time = list1[i]
        recommendation = list2[i]
        if (time in recommendation):
            counter += 1
    if (counter == len(list2)):
        return True
    else:
        return False
            

#Test code for leveling up over 30 'days'
leveling = Leveling_System([range(7, 10), range(12, 15), range(19, 22)], range(1100, 1301))

for i in range(30):
    time = []
    time.append(int(input("Enter when you ate breakfast ")))
    time.append(int(input("Enter when you ate lunch ")))
    time.append(int(input("Enter when you ate dinner ")))
    calories = int(input("Enter the total number of calories for today "))

    leveling.give_points(time, calories)
    leveling.level_up()

    print("Day:", i+1)
    print("Points:", leveling.getpoints())
    print("Level:", leveling.getlevel())