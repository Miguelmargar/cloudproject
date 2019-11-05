import os, json


class Events:
    
    def __init__(self):
        self.file_name = "events.json"
        self.search_file_name = "search_events.json"
        

    def show_events(self):
        
        self.check_if_db()
        
        if self.check_if_search() == False:
            with open(self.file_name) as self.file:
                self.data = json.load(self.file)
            self.file.close()
            return self.data
        else:
            with open(self.search_file_name) as self.file:
                self.data = json.load(self.file)
            self.file.close()

            os.remove(self.search_file_name)
            return self.data         
        
    
    
    def create_ev(self, name, date, desc):
        
        with open(self.file_name) as self.file:
            self.data = json.load(self.file)
            
            self.eventCount = len(self.data["events"])
            self.data["events"].append({
                                        "name":name, 
                                        "date":date,
                                        "desc":desc
                                        })
            self.file.close()
            
        with open(self.file_name, "w") as self.file:
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

        with open(self.search_file_name, "w") as self.search_file:
            json.dump(self.search_data, self.search_file)
        self.search_file.close()
        

    def check_if_db(self):
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
            
            
            
            
            
            
            
            