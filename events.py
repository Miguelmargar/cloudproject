import os, json, errno, time
from tweepy import OAuthHandler, API, Cursor, TweepError
from passw import *


class Events:
    flag = "no"
    s_data = None
    
    def __init__(self):
        self.user_name = ""
        self.user_password = ""
        self.main_file = "main.json"
        self.file_name = "events.json"
        self.search_file_name = "search_events.json"
        self.archive_name = "archive.json"
        self.check_if_db()

    def sign_user_up(self, name, passw):
        self.name = name
        self.passw = passw
        
        self.check_if_db()
        
        with open(self.main_file) as self.file:
            self.main_data = json.load(self.file)
        self.file.close()
        
        
        if self.name not in self.main_data["users"].keys():
            self.main_data["users"][self.name] = {"password": self.passw,
                                                  "events": [],
                                                  "searched": [],
                                                  "archived": []
                                                  }
                    
            with open(self.main_file, "w") as self.file:
                json.dump(self.main_data, self.file)
            self.file.close()
            return "created"
        else:
            return "exists"
            
    
    def log_user_in(self, name, passw):
        self.name = name
        self.passw = passw
        
        with open(self.main_file) as self.file:
            self.main_data = json.load(self.file)
        self.file.close()
        
        if self.name in self.main_data["users"].keys():
            if self.main_data["users"][self.name]["password"] == self.passw:
                
                if not os.path.exists(self.name + self.passw + ".json"):
                    self.new_file = open(self.name + self.passw + ".json", 'w+')
                    print("Database loaded")
                    self.new_file.close()
                    
                    with open(self.name + self.passw + ".json", "w") as self.file:
                        json.dump(self.main_data["users"][self.name], self.file)
                    self.file.close()
                
                return "loggedin"
            else:
                return "passerr"
        else:
            return "nameerr"
        
    
    def log_user_out(self, name, passw):
        self.name = name
        self.passw = passw
        
        with open(self.name + self.passw + ".json") as self.file:
            self.data_user = json.load(self.file)
        self.file.close()
  
        with open(self.main_file) as self.file:
            self.data = json.load(self.file)
        self.file.close()
                  
        self.data["users"][self.name] = self.data_user
        
        with open(self.main_file, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
         
        os.remove(self.name + self.passw + ".json")        
    
        
    def show_events(self, name, passw):
        self.name = name
        self.passw = passw
        
        
        
        with open(self.name + self.passw + ".json") as self.file:
            self.data = json.load(self.file)
        self.file.close()
                
#         if Events.flag == "no":
#             with open(self.file_name) as self.file:
#                 self.data = json.load(self.file)
#             self.file.close()
#             return self.data
#         elif Events.flag == "search" and self.check_if_search() == True:
#             with open(self.search_file_name) as self.file:
#                 self.data = json.load(self.file)
#             self.file.close()
#             time.sleep(0.5)
#             os.remove(self.search_file_name)
#             Events.flag = "no"
#         elif Events.flag == "archive":
#             with open(self.archive_name) as self.file:
#                 self.data = json.load(self.file)
#             self.file.close()
#             Events.flag = "no"
            
        return self.data         


    def create_ev(self, name, date, desc, file):
        
        with open(file) as self.file:
            self.data = json.load(self.file)
            
            self.eventCount = len(self.data["events"])
            self.data["events"].append({
                                        "name":name, 
                                        "date":date,
                                        "desc":desc
                                        })
            self.file.close()
            
        with open(file, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()

        
    def del_event(self, num):
        num = int(num)
        
        with open(self.file_name) as self.file:
            self.data = json.load(self.file)
             
            del self.data["events"][num] 
             
        self.file.close()
             
        with open(self.file_name, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()


    def del_event_sear(self, num):
        num = int(num)

        with open(self.file_name) as self.file:
            self.data = json.load(self.file)             
        self.file.close()

        for i, k in enumerate(self.data["events"]):
            if k == Events.s_data["events"][num]:
                del self.data["events"][i]
                          
        with open(self.file_name, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
        
        Events.s_data = None
 
    def del_event_arch(self, num):
        num = int(num)
        
        with open(self.archive_name) as self.file:
            self.data = json.load(self.file)
            
            del self.data["events"][num]
            
        self.file.close()
        
        with open(self.archive_name, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
        

    def edit_event(self, num, name, date, desc):
        num = int(num)
        
        with open(self.file_name) as self.file:
            self.data = json.load(self.file)

            if len(name) > 0:
                self.data["events"][num]["name"] = name

            if len(date) > 0:
                self.data["events"][num]["date"] = date

            if len(desc) > 0:
                self.data["events"][num]["desc"] = desc
        
        self.file.close()
             
        with open(self.file_name, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()


    def edit_event_sear(self, num, name, date, desc):
        num = int(num)
        
        with open(self.file_name) as self.file:
            self.data = json.load(self.file)             
        self.file.close()

        for i, k in enumerate(self.data["events"]):
            if k == Events.s_data["events"][num]:
                if len(name) > 0:
                    self.data["events"][i]["name"] = name
    
                if len(date) > 0:
                    self.data["events"][i]["date"] = date
    
                if len(desc) > 0:
                    self.data["events"][i]["desc"] = desc

        with open(self.file_name, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()


    def search_event(self, str):  
        
        with open(self.search_file_name) as self.file:
            self.search_data = json.load(self.file)
        self.file.close()      
        
        with open(self.file_name) as self.file:
            self.data = json.load(self.file)
        self.file.close()
        
        for i in self.data["events"]:
            if i["name"] == str:
                self.search_data["events"].append(i)

        if len(self.search_data["events"]) > 0:
            Events.flag = "search"
            Events.s_data = self.search_data

        with open(self.search_file_name, "w") as self.search_file:
            json.dump(self.search_data, self.search_file)
        self.search_file.close()
        

    def check_if_db(self):
        
        if not os.path.exists(self.main_file):
            self.new_file = open(self.main_file, 'w+')
            print("xxxxxx MAIN FILE CREATED xxxxxx")
            self.new_file.close()
            
            with open(self.main_file, "w") as self.file:
                json.dump({"users":{}}, self.file)
            self.file.close()
            
        if not os.path.exists(self.file_name):
            self.new_file = open(self.file_name, 'w+')
            print("xxxxxxxx FILE CREATED xxxxxxxx")
            self.new_file.close()
            
            with open(self.file_name, "w") as self.file:
                json.dump({"events":[]}, self.file)
            self.file.close()
            
        if not os.path.exists(self.search_file_name):
            self.new_file = open(self.search_file_name, 'w+')
            print("xxxx SEARCH FILE CREATED xxxx")
            self.new_file.close()
            
            with open(self.search_file_name, "w") as self.file:
                json.dump({"events":[]}, self.file)
            self.file.close()
            
        if not os.path.exists(self.archive_name):
            self.new_file = open(self.archive_name, 'w+')
            print("xxxx ARCIVE FILE CREATED xxxx")
            self.new_file.close()
            
            with open(self.archive_name, "w") as self.file:
                json.dump({"events":[]}, self.file)
            self.file.close()


    def check_if_search(self):
        
        if not os.path.exists(self.search_file_name):
            return False
        else:
            with open(self.search_file_name) as self.search_file:
                self.search_data = json.load(self.search_file)
                self.search_file.close()
                if len(self.search_data["events"]) > 0:
                    return True
                else:
                    return False
            
            
    def arch_eve(self, num):
        num = int(num)
        
        with open(self.file_name) as self.file:
            self.data = json.load(self.file) 
        self.file.close()     
        
        with open(self.archive_name) as self.file:
            self.a_data = json.load(self.file)  
        self.file.close()

        self.a_data["events"].append(self.data["events"][num])
        del self.data["events"][num]
        
        with open(self.file_name, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
        
        with open(self.archive_name, "w") as self.file:
            json.dump(self.a_data, self.file)
        self.file.close()
            
    
    def arch_eve_sear(self, num):
        num = int(num)    
        
        with open(self.archive_name) as self.file:
            self.a_data = json.load(self.file) 
            self.a_data["events"].append(Events.s_data["events"][num]) 
        self.file.close()
        
        with open(self.archive_name, "w") as self.file:
            json.dump(self.a_data, self.file)
        self.file.close()
        
        self.del_event_sear(num)
        
    
    def display_arch(self):
        Events.flag = "archive"
        
        
    def share_eve(self, num):
        num = int(num)
        
        try:
            auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
            auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
            api = API(auth)
            
            with open(self.file_name) as self.file:
                self.data = json.load(self.file)
            self.file.close()
            
            name = self.data["events"][num]["name"]
            when = self.data["events"][num]["date"]
            details = self.data["events"][num]["desc"]
    
            str = "New event: " + name + " on " + when + ". Details: " + details
            
            api.update_status(str)
        except TweepError as e:
            print(e)
            