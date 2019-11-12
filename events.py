import os, json


class Events:
    name = ""
    passw = ""
    login = ""
    file = ""
    sea = "no"
    arch = "no"
    share = "no"
    old_name = ""
    old_date = ""
    old_desc = ""
    sha_name = ""
    sha_date = ""
    sha_desc = ""
    
    def __init__(self):
        self.main_file = "main.json"
        self.check_if_db()

    
    
    def check_if_db(self):
        
        if not os.path.exists(self.main_file):
            self.new_file = open(self.main_file, 'w+')
            print("xxxxxx MAIN FILE CREATED xxxxxx")
            self.new_file.close()
            
            with open(self.main_file, "w") as self.file:
                json.dump({"users":{}}, self.file)
            self.file.close()
        
            
    def sign_user_up(self, name, passw):
        self.name = name
        self.passw = passw
                
        with open(self.main_file) as self.file:
            self.main_data = json.load(self.file)
        self.file.close()
        
        if self.name not in self.main_data["users"].keys():
            self.main_data["users"][self.name] = {"password": self.passw,
                                                  "events": [],
                                                  "searched": [],
                                                  "archived": [],
                                                  "shared_with": []
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
        
        Events.file = self.name + self.passw + ".json"
        Events.name = self.name
        Events.passw = self.passw
        
        with open(self.main_file) as self.file:
            self.main_data = json.load(self.file)
        self.file.close()
        
        if self.name in self.main_data["users"].keys():
            if self.main_data["users"][self.name]["password"] == self.passw:
                
                if not os.path.exists(Events.file):
                    self.new_file = open(self.name + self.passw + ".json", 'w+')
                    print("Database loaded")
                    self.new_file.close()
                    
                    with open(Events.file, "w") as self.file:
                        json.dump(self.main_data["users"][self.name], self.file)
                    self.file.close()
                Events.login = "loggedin"
                return "loggedin"
            else:
                Events.login = "passerr"
                return "passerr"
        else:
            Events.login = "nameerr"
            return "nameerr"
        
        
    def log_user_out(self):
        
        with open(Events.file) as self.file:
            self.data_user = json.load(self.file)
        self.file.close()
  
        with open(self.main_file) as self.file:
            self.data = json.load(self.file)
        self.file.close()
                  
        self.data["users"][self.name] = self.data_user
        
        with open(self.main_file, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
        
        os.remove(Events.file)
        
        Events.name = ""
        Events.passw = ""
        Events.login = ""
        Events.file = ""
         
        
    def create_ev(self, name, date, desc):
        
        with open(Events.file) as self.file:
            self.data = json.load(self.file)
            
            self.eventCount = len(self.data["events"])
            self.data["events"].append({
                                        "name":name, 
                                        "date":date,
                                        "desc":desc
                                        })
            self.file.close()
            
        with open(Events.file, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
        
    
    def show_events(self):
        
        with open(Events.file) as self.file:
            self.data = json.load(self.file)
        self.file.close()
        
        if Events.arch == "no" and Events.share == "no":
            if Events.sea == "no":
                return self.data["events"]
            
            elif Events.sea == "yes":
                temp_search = self.data["searched"] 
                self.clear_search()
                 
                return temp_search
                
        elif Events.arch == "yes":
            return self.data["archived"]  
        elif Events.share == "yes":
            return self.data["shared_with"]
            
    
    def del_event(self, event):

        section = "events"
        if event[-4:] == "arch":
            section = "archived"
            Events.arch = "yes"
            event = event[:-4]
        elif event[-5:] == "share":
            section = "shared_with"
            Events.share = "yes"
            event = event[:-5]
        
        with open(Events.file) as self.file:
            self.data = json.load(self.file)
        self.file.close()
        
        for i, k in enumerate(self.data[section]):
            if str(k) == event:
                del self.data[section][i]
        
        with open(Events.file, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
        
        
    def search(self, word):
        
        with open(Events.file) as self.file:
            self.data = json.load(self.file)
        self.file.close()
        
        for i in self.data["events"]:
            if i["name"] == word:
                self.data["searched"].append(i)
                
        with open(Events.file, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
        
        Events.sea = "yes"
   
        
    def clear_search(self):
        
        with open(Events.file) as self.file:
            self.data = json.load(self.file)
        self.file.close()
        
        self.data["searched"] = []
        
        with open(Events.file, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
        
    
    def get_old_details(self, old_name, old_date, old_desc):
        Events.old_name = old_name
        Events.old_date = old_date
        Events.old_desc = old_desc
    
    
    def edit_event(self, name, date, desc):
        
        with open(Events.file) as self.file:
            self.data = json.load(self.file)
        self.file.close()
        
        for i, k in enumerate(self.data["events"]):
            if k["name"] == Events.old_name and k["date"] == Events.old_date and k["desc"] == Events.old_desc:
                
                if len(name) > 0:
                    self.data["events"][i]["name"] = name
    
                if len(date) > 0:
                    self.data["events"][i]["date"] = date
    
                if len(desc) > 0:
                    self.data["events"][i]["desc"] = desc
        
        with open(Events.file, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()
        
        
    def arch_eve(self, event): 
               
        with open(Events.file) as self.file:
            self.data = json.load(self.file) 
        self.file.close()     

        for i, k in enumerate(self.data["events"]):
            if str(k) == event:
                self.data["archived"].append(self.data["events"][i])
                del self.data["events"][i]
        
        with open(Events.file, "w") as self.file:
            json.dump(self.data, self.file)
        self.file.close()   
        
        
    def show_arch(self):
        Events.arch = "yes"
        
   
    def get_share_details(self, name, date, desc):
        Events.sha_name = name
        Events.sha_date = date
        Events.sha_desc = desc
   
        
    def share_with(self, user):
        
        with open(self.main_file) as self.file:
            self.main_data = json.load(self.file) 
        self.file.close()
        
        if user in self.main_data["users"].keys():
             
            self.main_data["users"][user]["shared_with"].append({
                                        "name": Events.sha_name, 
                                        "date": Events.sha_date,
                                        "desc": Events.sha_desc,
                                        "from": Events.name,
                                        "to": user
                                        })
            with open(self.main_file, "w") as self.file:
                json.dump(self.main_data, self.file)
            self.file.close()
        
            return True

        else:
            return False
            
    
    def show_shared_with(self):
        Events.share = "yes"
    
        
        
        
        