# import datetime
import datetime 

class Login:
    start_date = datetime.datetime(2022,1,9,18,00,00) #assuming this is when the user starts using the app
    #print(start_date.day)
    current_datetime = datetime.datetime.now()#the current time 
    #print(current_datetime.day)

    #Daily Login Rewards are stored in an array
    daily_login_rewards = ["100 gold coins", "200 gold coins", "5 diamonds", "300 gold coins", "boarder #1", "10 diamonds", "skin #1"]
    login_status = 1 # 0 = off; 1 = on
    reward_status = 1 # 0 = reward has been claimed by the user; 1 = reward has not yet been claimed

    def __init__(self):
        pass

    def set_login_status(self, status):
        self.login_status = status

    def set_reward_status(self, status):
        self.reward_status = status
    
    #User could claim rewards by logging into the application daily
    #Rewards contain gold coin (currency of the app), diamonds (special currency of the app), boarders (decorations for the user), skins for "Mini Figure"
    def daily_login(self, num_login_days, currency, diamonds, skins, special_boarder):
        if self.login_status == 1 and self.reward_status == 1:
            print("working")
            if num_login_days == 0:
                print("Here is your daily login reward: " + self.daily_login_rewards[num_login_days])
                if self.daily_login_rewards[num_login_days] == "100 gold coins":
                    currency += 100
                    self.reward_status = 0
            
            if num_login_days >= 1 and num_login_days <= 5:
                if self.current_datetime.day - self.start_date.day >= 1: #making sure the number of login days are updated correctly
                #print(current_datetime.day - start_date.day)
                #NOTE that when >= here is to test the program more conveniently withou waiting for days to change during testing
                #he
                    print("Here is your daily login reward: " + self.daily_login_rewards[num_login_days])        
                    if self.daily_login_rewards[num_login_days] == "100 gold coins":
                        currency += 100
                    if self.daily_login_rewards[num_login_days] == "200 gold coins":
                        currency += 200    
                    if self.daily_login_rewards[num_login_days] == "300 gold coins":
                        currency += 300
                    if self.daily_login_rewards[num_login_days] == "5 diamonds":
                        diamonds += 5
                    if self.daily_login_rewards[num_login_days] == "10 diamonds":
                        diamonds += 10
                    if self.daily_login_rewards[num_login_days] == "boarder #1":
                    #boarder = 1, user has the item; boarder = 0, user doesn not have access to that item
                        special_boarder.append("boarder #1")
                        self.reward_status = 0

            if num_login_days == 6:
                if self.current_datetime.day - self.start_date.day >= 1: #making sure the number of login days are updated correctly
                    print("Here is your daily login reward: " + self.daily_login_rewards[num_login_days])
                    if self.daily_login_rewards[num_login_days] == "skin #1":
                            #if skin is in the list, the user has the item; if not 0, user doesn not have access to that item
                            skins.append("skin #1")
                            self.reward_status = 0
                            num_login_days == 0
                            #start_date = datetime.datetime.now()
                            #this is used to update the start_time,commented for testing purpouses
                            return currency, diamonds, special_boarder, skins, num_login_days  #Only a demonstration of this function is working correctly

            num_login_days += 1
            #start_date = datetime.datetime.now()
            #this is used to update the start_time, commented for testing purpouses
            return currency, diamonds, special_boarder, skins, num_login_days #Only a demonstration of this function is working correctly


        elif self.login_status == 1 and self.reward_status == 0:
            print("You have already claimed the daily reward!")
            return currency, diamonds, special_boarder, skins, num_login_days

        else:
            print("Not logged in")
            
            
    def current_belongings(self, currency, diamonds, special_boarder, skins):
        print("You currently have " + str(currency) + " gold coins, " + str(diamonds) + " diamonds. ")
        print("You have accesory items: ")
        for i in range(len(special_boarder)):
                print(str(special_boarder[i]))
        for i in range(len(skins)):
                print(str(skins[i]))
        

#Test Case
currency = 0
diamonds = 0
special_boarder = []
skins = []
num_login_days = 1

login = Login()

currency, diamonds, special_boarder, skins, num_login_days = login.daily_login(num_login_days, currency, diamonds, skins, special_boarder)
login.current_belongings(currency, diamonds, special_boarder, skins)

num_login_days = 4
currency, diamonds, special_boarder, skins, num_login_days = login.daily_login(num_login_days, currency, diamonds, skins, special_boarder)
login.current_belongings(currency, diamonds, special_boarder, skins)

num_login_days = 5
currency, diamonds, special_boarder, skins, num_login_days = login.daily_login(num_login_days, currency, diamonds, skins, special_boarder)
login.current_belongings(currency, diamonds, special_boarder, skins)

num_login_days = 6
currency, diamonds, special_boarder, skins, num_login_days = login.daily_login(num_login_days, currency, diamonds, skins, special_boarder)
login.current_belongings(currency, diamonds, special_boarder, skins)