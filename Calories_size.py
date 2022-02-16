
from numpy import size


def Pick_Size(Food): #Picking up the numbers of Calories inside the list
    Calories_List = []
    for i in Food:
        Calories_List.append(i[1])
    print(Calories_List)
    return Calories_List

def Calories_Size(Calories):#Picking from small, median and large
    size_list = ["Small", "Medium", "Large", "Large"]
    x = 0
    Update_List = []
    for i in Calories:
        if size_list[x] == "Small":
                i *= 0.5
        if size_list[x] == "Medium":
                i *= 1
        if size_list[x] == "Large":
                i *= 2
        x += 1
        Update_List.append(i)
        print(Update_List)
    return Update_List

def Calorie_Adjustement(food_list):
    size = Pick_Size(food_list)
    calorie_list = Calories_Size(size)
    return calorie_list

Breakfast_Food_Choice = [["Apple",52], ["Banana",62], ["Orange",42], ["Burgers",74]] #Examples of if the user picked this amount of food
Calories_List = Pick_Size(Breakfast_Food_Choice)
Calories_Size(Calories_List)