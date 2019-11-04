import os, json

class Events:
    
    def __init__(self):
        self.file_name = "events.json"

    def show_events(self):
        
        self.check_if_any()
        
        with open(self.file_name) as self.file:
            self.data = json.load(self.file)
            return self.data["events"]
        self.file.close()
    
            
    
    
    def create_event(self):
        
        self.check_if_any()
            
#         with open(self.file_name, "w") as self.file:

            

    def check_if_any(self):
        if not os.path.exists(self.file_name):
            self.new_file = open(self.file_name, 'w+')
            print("xxxxxxxx FILE CREATED xxxxxxxx")
            self.new_file.close()
            
            with open(self.file_name, "w") as self.file:
                json.dump({"events":[]}, self.file)
            self.file.close()