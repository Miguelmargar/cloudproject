import os, pymysql, sys, hashlib, binascii, re
from passw import *


class Events:
    
    def __init__(self):
        None
    
    def sign_user_up(self, name, passw):
        user = db_user
        password = db_key
        host = db_host
        database = db_name
        
        passw = self.hash_password(passw)
        
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
                insert = """INSERT INTO users (user_name, password)
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
        user = db_user
        password = db_key
        host = db_host
        database = db_name
         
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
            state = "nameerr"
         
        query = """SELECT password
                FROM eventmanager.users
                WHERE eventmanager.users.user_name = %s"""
                      
        cur = con.cursor()
        cur.execute(query, (name),)
        data = cur.fetchall()
        cur.close()

        if len(data) < 1 or not self.verify_password(data[0][0], passw):
            state = "passerr"
        
        state = "loggedin"
        
        return state

        
    def create_ev(self, name, date, time, descr, user_name):
        user = db_user
        password = db_key
        host = db_host
        database = db_name
        
        if time == "" or time == "00:00":
            time = "All Day" 
        
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)

        insert = "INSERT INTO events (user_name,name,date,time,descr) VALUES (%s,%s,%s,%s,%s);"
        
        cur = con.cursor()
        cur.execute(insert, (user_name,name,date,time,descr),)
        cur.close()
        con.commit()
        
    
    def show_events(self, name, login, *args):
        user = db_user
        password = db_key
        host = db_host
        database = db_name
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        if login == "loggedin":
            
            query = """SELECT name, DATE_FORMAT(date, '%d-%m-%Y'), time, descr
                    FROM events
                    WHERE events.user_name = '""" + name + "';"

            try:
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                cur.close()
                return data
            except:
                return ()
                            
        elif login == "loginsea":
            if "'" in args[0]:
                quote = "\""
            else:
                quote = "\'"
            
            query = """SELECT name, DATE_FORMAT(date, '%d-%m-%Y'), time, descr
                    FROM events
                    WHERE events.name = """ + quote + args[0] + quote + " and events.user_name = '" + name + "';"

            try:
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                cur.close()
                return data
            except:
                return ()
                                 
        elif login == "loginarch":
            query = """SELECT name, DATE_FORMAT(date, '%d-%m-%Y'), time, descr
                        FROM archived
                        WHERE archived.user_name = '""" + name + "';"
            try:
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                cur.close()
                return data
            
            except:
                return ()  
        
        elif login == "loginsha":
            query = """SELECT name, DATE_FORMAT(date, '%d-%m-%Y'), time, descr, fromName
                    FROM shared_with
                    WHERE shared_with.toName = '""" + name + "';"
            try:
                cur = con.cursor()
                cur.execute(query)
                data = cur.fetchall()
                cur.close()
                return data
            except:
                return ()
            
    
    def del_event(self, info):
        user = db_user
        password = db_key
        host = db_host
        database = db_name

        pat = r"\"(.*?)\"|'(.*?)'"
        info = re.findall(pat, info)

        final = []
        for i in info:
            empty = True
            for j in i:
                if len(j) > 0:
                    final.append(j.replace("'", "\\'"))
                    empty = False
            if empty == True:
                final.append('')
        info = final
        
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        section = "events"
        if info[5] == "loginarch":
            section = "archived"
        elif info[5] == "loginsha":
            section = "shared_with"
        
        name = info[0]
        date = self.format_date(info[1])
        time = info[2]
        descr = info[3]    
        
        if info[5] == "loggedin" or info[5] == "loginsea" or info[5] == "loginarch":
            delete = "DELETE FROM " + section + " WHERE user_name='" + info[4] + "' and name='"+ name + "' and date='" + date +  "' and time='" + time + "' and descr='" + descr + "';"
        else:
            delete = "DELETE FROM " + section + " WHERE name='"+ name + "' and date='" + date + "' and time='" + time + "' and descr='" + descr + "' and fromName='" + info[6] + "' and toName='" + info[4] + "';" 
        
        cur = con.cursor()
        cur.execute(delete)
        cur.close()
        con.commit()
        
        return [info[4], info[5]]
        
    
    def edit_event(self, name, date, time, descr, old_details):
        user = db_user
        password = db_key
        host = db_host
        database = db_name

        old_details = old_details.split("*,")
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        old_details[1] = self.format_date(old_details[1])
        date = self.format_date(date)
        
        if time == "" or time == "00:00":
            time = "All Day"
        
        update = "UPDATE events SET name = '" + name + "', date = '" + date + "', time = '" + time + "', descr = '" + descr + "' WHERE name = '" + old_details[0] + "' and user_name = '" + old_details[4] + "' and date = '" + old_details[1] + "' and time = '" + old_details[2] + "' and descr = '" + old_details[3] + "'"
        cur = con.cursor()
        cur.execute(update)
        cur.close()
        con.commit()

        
    def arch_eve(self, info):
        self.info = info 
        user = db_user
        password = db_key
        host = db_host
        database = db_name
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)

        pat = r"\"(.*?)\"|'(.*?)'"
        info = re.findall(pat, info)
        
        final = []
        for i in info:
            empty = True
            for j in i:
                if len(j) > 0:
                    final.append(j.replace("'", "\\'"))
                    empty = False
            if empty == True:
                final.append('')
        info = final
        
        name = info[0]
        date = self.format_date(info[1])
        time = info[2]
        descr = info[3]
         
        insert = "INSERT INTO archived (user_name,name,date,time,descr) VALUES (%s,%s,%s,%s,%s);"
        cur = con.cursor()
        cur.execute(insert, (info[4], name, date, time, descr),)
        cur.close()
        con.commit()       
        
        self.del_event(self.info) # check self.info for concurrency issues
   
        return info[4]
   
        
    def share_with(self, user_sha, user_eve):
        user = db_user
        password = db_key
        host = db_host
        database = db_name
         
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
        
        details = user_eve.split("*,")

        if len(data) < 1 or data[0][0] != user_sha:
            return "False"
        else:
            insert = "INSERT INTO shared_with (name, date, time, descr, fromName, toName) VALUES (%s, %s, %s, %s, %s, %s)"
            cur = con.cursor()
            cur.execute(insert, (details[0], self.format_date(details[1]), details[2], details[3], details[4], user_sha),)
            cur.close()
            con.commit()
            return "True"       
            
        
#     make the format of the date to yyyy-mm-dd
    def format_date(self, date):
        date = date.split("-")
        date = [date[2], date[1], date[0]]
        date = "-".join(date)
        return date   
    
    
    def hash_password(self, password):
        """Hash a password for storing."""
        
        salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
        
        pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
        
        pwdhash = binascii.hexlify(pwdhash)
        
        return (salt + pwdhash).decode('ascii')
    
    
    def verify_password(self, stored_password, provided_password):
        """Verify a stored password against one provided by user"""
        
        salt = stored_password[:64]
        
        stored_password = stored_password[64:]
        
        pwdhash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), 
                salt.encode('ascii'), 100000)
        
        pwdhash = binascii.hexlify(pwdhash).decode('ascii')
        
        return pwdhash == stored_password
    
    
    def change_user_pic(self, new_pic, user):
        user = db_user
        password = db_key
        host = db_host
        database = db_name
         
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        query = """SELECT photo
                FROM users
                WHERE user_name = %s"""
        
        cur = con.cursor()
        cur.execute(query, (user),)
        data = cur.fetchall()
        cur.close()
        
        print(data)
        
        
        
        
        