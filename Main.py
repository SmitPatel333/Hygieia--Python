from datetime import datetime
from Calories_Calculation import Calories_Calculation
from Calories_size import *
from Character import Character
from Leveling import *
from Login import Login

class Main:
    little_H = Character(Leveling_System([range(7, 10), range(12, 15), range(19, 22)], range(1100, 1301)), 1)
    Calorie_Calculator = Calories_Calculation()
    Login_System = Login()
    Materials = [1, 0, 0, [], []] #List of materials for login. In order: Login Day, Currency, Diamonds, Skins, Special Boarder

    def __init__(self):
        pass

    def login_reward(self):
        self.Login_System.set_login_status(1)
        self.Login_System.daily_login(self.Materials)
        self.Login_System.current_belongings(self.Materials[1:])
    
    def eat_food(self, meal_type, foods):
        #Food_List = [["Apple",52], ["Banana",62], ["Orange",42], ["Burgers",74]] In the app, the player will choose this list
        Food_List = foods
        refined_list = Calorie_Adjustement(Food_List)

        if(meal_type.lower == "breakfast"):
            self.Calorie_Calculator.Breakfast_Calories(refined_list)
        elif(meal_type.lower == "lunch"):
            self.Calorie_Calculator.Lunch_Calories(refined_list)
        elif(meal_type.lower == "dinner"):
            self.Calorie_Calculator.Dinner_Calories(refined_list)
        elif(meal_type.lower == "snack"):
            self.Calorie_Calculator.Snack_Calories(refined_list)
        
        time = datetime.now().hour
        self.little_H.update_time_eaten(time)

    def calorie_total(self):
        self.Calorie_Calculator.Final_Calories()
        self.little_H.update_total_calories(self.Calorie_Calculator.get_Total_Calories)

    def end_day(self):
        self.calorie_total()
        self.little_H.end_of_day()
        self.Calorie_Calculator.reset()
        self.Login_System.set_reward_status(1)
        if self.Materials[0] == 6:
            self.Materials[0] = 0
        else:
            self.Materials[0] +=1