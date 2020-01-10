from flask import Flask, flash, render_template, redirect, request, url_for
from events import *
from threading import Lock

app = Flask(__name__)
app.secret_key = flash_key
app.config['TESTING'] = True

@app.route('/')
def index():
    global a
    a = Events()
    
    global lock
    lock = Lock()
    
    return render_template("index.html")

@app.route("/signUp", methods=['POST'])
def sign_user():
    signLock = Lock()
    signLock.acquire()
    name = request.form.get("signName")
    passw = request.form.get("signPass")
    
    sign = a.sign_user_up(name, passw)
    
    if sign == "created":
        flash("%s, Your Account Has Been Created" % name.capitalize(), "good")
    elif sign == "exists":
        flash("Name '%s' Is Already Taken, Please Try a Different One!" % name, "error")
    signLock.release()
    return redirect("/")


@app.route("/logIn", methods=['POST'])
def log_user():
    lock.acquire()
    name = request.form.get("logName")
    passw = request.form.get("logPass")
    
    login = a.log_user_in(name, passw)
    
    if a.login == "loggedin":
        return redirect("/show_main")
    elif a.login == "nameerr":
        flash("ACCOUNT DOES NOT EXISTS - PLEASE TRY A DIFFERENT NAME", "error")
        lock.release()
        return redirect("/")
    elif a.login == "passerr":
        flash("WRONG PASSWORD - PLEASE TRY CHECKING YOUR PASSWORD", "error")
        lock.release()
        return redirect("/")
    
@app.route("/show_main")
def show_main():
    login = a.login
    name = a.name
    events = a.show_events()

    a.login = ""
    a.name = ""
    lock.release()
    return render_template("/in.html", login=login, name=name, events=events)

@app.route("/home", methods=['GET'])
def home():
    lock.acquire()
    details = request.args.get('value')
    
    pat = r"'(.*?)'"
    details = re.findall(pat, details)
    
    print(details)

    a.name = details[0]
    a.login = details[1]
    
    return redirect("/show_main")


@app.route("/createEvent", methods=['POST'])
def create_event():
    lock.acquire()
    name = request.form.get('name')
    date = request.form.get('date')
    time = request.form.get('time')
    desc = request.form.get('desc')
    user_det = request.form.get('cre_event')

    a.create_ev(name, date, time, desc, user_det)
    
    return redirect("/show_main")


@app.route("/deleteEvent", methods=['POST'])
def delete_event():
    lock.acquire()
    info = request.form["delete"]

    a.del_event(info)
    
    flash("Task Deleted Successfully!", "good")
    
    return redirect("/show_main")
    

@app.route("/logOut", methods=['GET'])
def log_user_out():  
    
    flash("You Have Successfully Logged Out", "good")
    
    return redirect("/")


@app.route("/searchEvent", methods=['POST'])
def search_event():
    lock.acquire()
    word = request.form.get('search')
    user_name = request.form.get('sea_deta')

    a.search(word)
    a.name = user_name

    return redirect("/show_main")
    

@app.route("/edit_event", methods=['POST'])
def edit_event():
    lock.acquire()
    new_name = request.form.get('edName')
    new_date = request.form.get('edDate')
    new_time = request.form.get('edTime')
    new_desc = request.form.get('edDesc')
    old_details = request.form.get('ed_event')
    
    a.edit_event(new_name, new_date, new_time, new_desc, old_details)
     
    return redirect("/show_main")


@app.route("/archive_event", methods=['POST'])
def archive_event():
    lock.acquire()
    info = request.form["archive"]
        
    a.arch_eve(info)
    
    flash("Task Successfully Archived!", "good")

    return redirect("/show_main")


@app.route("/show_archive")
def show_archive():
    lock.acquire()
    name = request.args.get('value')
    
    a.show_arch(name)
    
    return redirect("/show_main")


@app.route("/share_with", methods=['POST'])
def share_with():
    lock.acquire()
    share_user = request.form.get('shareName')
    share_details = request.form.get('sha_event')
    
    is_shared = a.share_with(share_user, share_details)
    
    if is_shared == True:
        flash("Your Event has been shared with '%s'" % share_user, "good")
    else:
        flash("Error Sharing, Name '%s' does not exist, please check for spelling mistakes" % share_user, "error")
    
    return redirect("/show_main")
 
 
@app.route("/show_shared_with")
def show_shared_with():
    lock.acquire()
    name = request.args.get('value')
     
    a.show_shared_with(name)
     
    return redirect("/show_main")

    
    
if __name__ == '__main__':
    app.run(debug=True)