
class Calories_Calculation():
    Breakfast_Calories_Total = 0
    Lunch_Calories_Total = 0
    Dinner_Calories_Total = 0
    Snack_Calories_Total = 0
    Total_Calories = 0

    def __init__(self):
        pass

    def get_Breakfast_Calories(self):
        return self.Breakfast_Calories

    def get_Lunch_Calories(self):
        return self.Lunch_Calories

    def get_Dinner_Calories(self):
        return self.Dinner_Calories

    def get_Snack_Calories(self):
        return self.Snack_Calories
    
    def get_Total_Calories(self):
        return self.Total_Calories

    def reset(self):
        self.Breakfast_Calories_Total = 0
        self.Lunch_Calories_Total = 0
        self.Dinner_Calories_Total = 0
        self.Snack_Calories_Total = 0
        self.Total_Calories = 0

    def Breakfast_Calories(self, Breakfast_Selected_Item):
        self.Breakfast_Calories_Total = sum(Breakfast_Selected_Item)

        if self.Breakfast_Calories_Total == 360:
            print ("Wow, perfectly balanced like everything should be.")     #I found a send.notification module that works with Android, we might be able to switch to that later on.
        elif self.Breakfast_Calories_Total < 360:
            print ("MORE! I want MORE!")
        elif self.Breakfast_Calories_Total > 360:
            print ("Hold up! I don't want to get diabetes.")
    

    def Lunch_Calories(self, Lunch_Selected_Item):
        self.Lunch_Calories_Total = sum(Lunch_Selected_Item)

        if self.Lunch_Calories_Total == 480:
            print ("Wow, perfectly balanced like everything should be.")
        elif self.Lunch_Calories_Total < 480:
            print ("I want MOREEEEEEEEEEE!")
        elif self.Lunch_Calories_Total > 480:
            print ("That's too much. qAq")
    
    def Dinner_Calories(self, Dinner_Selected_Item):
        self.Dinner_Calories_Total = sum(Dinner_Selected_Item)

        if self.Dinner_Calories_Total == 360:
            print ("Perfectly Balance~")
        elif self.Dinner_Calories_Total < 460:
            print ("You need to eat more!")
        elif self.Dinner_Calories_Total > 460:
            print ("woo...You are not trying to get diabetes, right?")
    
    def Snack_Calories(self, Snack_Selected_Item):
        self.Snack_Calories_Total = sum(Snack_Selected_Item)
    
    def Final_Calories(self):
        #Adding up every Total together
        self.Total_Calories = self.Dinner_Calories_Total + self.Lunch_Calories_Total + self.Breakfast_Calories_Total + self.Snack_Calories_Total

        if self.Total_Calories > 1100 and self.Total_Calories < 1300 : #within the range of 1100 to 1300
            print ("Fitness is my passion!")
        elif self.Total_Calories < 1100:
            print ("I need MOREEEE!")
        elif self.Total_Calories > 1300:
            print ("I am so fat... No bodys gonna like me... qAq")