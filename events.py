import os, json

class Events:
    
    def __init__(self):
        self.file_name = "events.json"
        self.eventCount = 0

    def show_events(self):
        
        self.check_if_any()
        
        with open(self.file_name) as self.file:
            self.data = json.load(self.file)
        self.file.close()
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


    def check_if_any(self):
        if not os.path.exists(self.file_name):
            self.new_file = open(self.file_name, 'w+')
            print("xxxxxxxx FILE CREATED xxxxxxxx")
            self.new_file.close()
            
            with open(self.file_name, "w") as self.file:
                json.dump({"events":[]}, self.file)
            self.file.close()
            
            

            