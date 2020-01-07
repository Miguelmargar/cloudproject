import os, pymysql, sys
from passw import *
from test.datetimetester import DAY


class Events:
    
    def __init__(self):
        self.name = ""
        self.login = ""
            
            
    def sign_user_up(self, name, passw):
        user = dbuser
        password = db_key
        host = dbhost
        database = dbname
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
            
        query = """SELECT user_name
                FROM eventmanager.users
                WHERE eventmanager.users.user_name = %s
                    and eventmanager.users.password = %s"""   
        
        cur = con.cursor()
        cur.execute(query, (name, passw),)
        data = cur.fetchall()
        cur.close()
        
        if len(data) > 0:
            return "exists"
        elif len(data) == 0:
            try:
                insert = """INSERT INTO users ( user_name, password)
                            VALUES
                            (%s, %s);"""
                
                cur = con.cursor()
                cur.execute(insert, (name, passw),)
                cur.close()
                con.commit()
                return "created"
            except:
                return "exists"
        
        
    def log_user_in(self, name, passw):
        user = dbuser
        password = db_key
        host = dbhost
        database = dbname
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        
        query = """SELECT user_name
                FROM users
                WHERE users.user_name = %s"""
                    
        cur = con.cursor()
        cur.execute(query, (name),)
        data = cur.fetchall()
        cur.close()
        
        if len(data) < 1 or data[0][0] != name:
            self.login = "nameerr"
            return "nameerr"
         
        query = """SELECT password
                FROM eventmanager.users
                WHERE eventmanager.users.password = %s"""
                      
        cur = con.cursor()
        cur.execute(query, (passw),)
        data = cur.fetchall()
        cur.close()

        if len(data) < 1 or data[0][0] != passw:
            self.login = "passerr"
            return "passerr"
        
        self.name = name
        self.login = "loggedin"
        
        
    def log_user_out(self):
        self.name = ""
        self.login = ""

        
    def create_ev(self, name, date, time, descr, user_det):
        user = dbuser
        password = db_key
        host = dbhost
        database = dbname
        
        user_det = user_det.replace("'", "")
        user_det = user_det[1:-1].split(",")
        user_det = [i.strip() for i in user_det]
        
        date = date.split("-")
        date = [date[2], date[1], date[0]]
        date = "-".join(date)

        if time == "" or time == "00:00":
            time = "All Day" 
        
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)

        insert = "INSERT INTO events (user_name,name,date,time,descr) VALUES (%s,%s,%s,%s,%s);"
        
        cur = con.cursor()
        cur.execute(insert, (user_det[0],name,date,time,descr),)
        cur.close()
        con.commit()
        
        self.name = user_det[0]
        self.login = user_det[1]
        
    
    def show_events(self):
        user = dbuser
        password = db_key
        host = dbhost
        database = dbname
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        if self.login == "loggedin":
            query = """SELECT name, date, descr
                    FROM events
                    WHERE events.user_name = %s"""
            try:
                cur = con.cursor()
                cur.execute(query, (self.name),)
                data = cur.fetchall()
                cur.close()
                return data
            except:
                return ()
                            
        elif self.login == "loginsea":
            query = """SELECT name, date, descr
                    FROM events
                    WHERE events.name = %s
                    and events.user_name = %s"""
            try:
                cur = con.cursor()
                cur.execute(query, (self.sea_word, self.name),)
                data = cur.fetchall()
                cur.close()
                return data
            except:
                return ()
                                 
        elif self.login == "loginarch":
            query = """SELECT name, date, descr
                        FROM archived
                        WHERE archived.user_name = %s"""
            try:
                cur = con.cursor()
                cur.execute(query, (self.name),)
                data = cur.fetchall()
                cur.close()
                return data
            
            except:
                return ()  
        
        elif self.login == "loginsha":
            query = """SELECT name, date, descr, fromName
                    FROM shared_with
                    WHERE shared_with.toName = %s"""
            try:
                cur = con.cursor()
                cur.execute(query, (self.name),)
                data = cur.fetchall()
                cur.close()
                return data
            except:
                return ()
            
    
    def del_event(self, info):
        user = dbuser
        password = db_key
        host = dbhost
        database = dbname

        info = info.replace("'", "").replace("\"", "")
        info = info[1:-1].split(",")
        info = [i.strip() for i in info]
        
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        section = "events"
        if info[4] == "loginarch":
            section = "archived"
        elif info[4] == "loginsha":
            section = "shared_with"

        name = info[0]
        date = info[1]
        descr = info[2]    
        
        if info[4] == "loggedin" or info[4] == "loginsea" or info[4] == "loginarch":
            delete = "DELETE FROM " + section + " WHERE user_name='" + info[3] + "' and name='"+ name + "' and date='" + date + "' and descr='" + descr + "';" 
        else:
            delete = "DELETE FROM " + section + " WHERE name='"+ name + "' and date='" + date + "' and descr='" + descr + "' and fromName='" + info[5] + "' and toName='" + info[3] + "';" 
        
        cur = con.cursor()
        cur.execute(delete)
        cur.close()
        con.commit()
        
        self.name = info[3]
        self.login = info[4]
        
        
    def search(self, word):
        self.sea_word = word
        self.login = "loginsea"
    
    
    def edit_event(self, name, date, descr, old_details):
        user = dbuser
        password = db_key
        host = dbhost
        database = dbname
        
        old_details = old_details.split(",")
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        update = "UPDATE events SET name = '" + name + "', date = '" + date + "', descr = '" + descr + "' WHERE name = '" + old_details[0] + "' and user_name = '" + old_details[3] + "' and date = '" + old_details[1] + "' and descr = '" + old_details[2] + "'"
        cur = con.cursor()
        cur.execute(update)
        cur.close()
        con.commit()

        self.name = old_details[3]
        self.login = old_details[4]
        
        
    def arch_eve(self, info):
        self.info = info 
        user = dbuser
        password = db_key
        host = dbhost
        database = dbname
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        info = info.replace("'", "")
        info = info[1:-1].split(",")
        info = [i.strip() for i in info]
        
        name = info[0]
        date = info[1]
        descr = info[2]
         
        insert = "INSERT INTO archived (user_name,name,date,descr) VALUES (%s,%s,%s,%s);"
        cur = con.cursor()
        cur.execute(insert, (info[3], name, date, descr),)
        cur.close()
        con.commit()       
        
        self.del_event(self.info)
        
    def show_arch(self, name):
        self.login = "loginarch"
        name = name.replace("'", "")
        self.name = name
        
    def share_with(self, user_sha, user_eve):
        user = dbuser
        password = db_key
        host = dbhost
        database = dbname
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        query = """SELECT user_name
                FROM users
                WHERE users.user_name = %s"""

        cur = con.cursor()
        cur.execute(query, (user_sha),)
        data = cur.fetchall()
        cur.close()
        
        details = user_eve.split(",")

        if len(data) < 1 or data[0][0] != user_sha:
            self.name = details[3]
            self.login = details[4]
            return False
        else:
            insert = "INSERT INTO shared_with (name, date, descr, fromName, toName) VALUES (%s, %s, %s, %s, %s)"
            cur = con.cursor()
            cur.execute(insert, (details[0], details[1], details[2], details[3], user_sha),)
            cur.close()
            con.commit()
            self.name = details[3]
            self.login = details[4]
            return True       
            
    
    def show_shared_with(self, name):
        self.login = "loginsha"
        name = name.replace("'", "")
        self.name = name
        
        
        
        