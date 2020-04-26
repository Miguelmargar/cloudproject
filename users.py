from passw import *
import pymysql, hashlib, binascii, os, sys
from werkzeug.utils import secure_filename


class Users:
    
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
            return state
         
        query = """SELECT password
                FROM eventmanager.users
                WHERE eventmanager.users.user_name = %s"""
                      
        cur = con.cursor()
        cur.execute(query, (name),)
        data = cur.fetchall()
        cur.close()

        if len(data) < 1 or not self.verify_password(data[0][0], passw):
            state = "passerr"
            return state
        
        state = "loggedin"
        
        return state   
    
    
    def check_pic(self, name):
        user = db_user
        password = db_key
        host = db_host
        database = db_name
        
        try:
            con = pymysql.connect(host=host, database=database, user=user, password=password)
        except Exception as e:
            sys.exit(e)
        
        query = """SELECT photo, photo_name
                FROM users
                WHERE user_name = %s"""
                    
        cur = con.cursor()
        cur.execute(query, (name),)
        data = cur.fetchall()
        cur.close()
        
        if len(data) > 0 and data[0][0] == "yes":
            return data[0][1]
        elif len(data) > 0 and data[0][0] == "no":
            return data[0][0]
        else:
            return "no"
        
    
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
    
    
    def change_user_pic(self, user_photo, user_name):
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
        cur.execute(query, (user_name),)
        data = cur.fetchall()
        cur.close()
        
        filename = user_name + "." + secure_filename(user_photo.filename).split(".")[1]
        filename = filename.replace("'","\\'")
        user_name = user_name.replace("'","\\'")
        
        if data[0][0] == "no":
            update = "UPDATE users SET photo = 'yes', photo_name = '" + filename + "' WHERE user_name = '" + user_name + "'"
        elif data[0][0] == "yes":
            update = "UPDATE users SET photo_name = '" + filename + "' WHERE user_name = '" + user_name + "'"
        
        cur = con.cursor()
        cur.execute(update)
        cur.close()
        con.commit()
         
        filename = filename.replace("\\'","'")
        user_photo.save(os.path.join("static/assets/", filename))
         
        return filename