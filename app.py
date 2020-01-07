from flask import Flask, flash, render_template, redirect, request, url_for
from events import *
from ctypes.test.test_pickling import name



app = Flask(__name__)
app.secret_key = flash_key
app.config['TESTING'] = True

@app.route('/')
def index():
    global a
    a = Events()
    
    return render_template("index.html")

@app.route("/signUp", methods=['POST'])
def sign_user():
    name = request.form.get("signName")
    passw = request.form.get("signPass")
    
    sign = a.sign_user_up(name, passw)
    
    if sign == "created":
        flash("%s, Your Account Has Been Created" % name.capitalize(), "good")
    elif sign == "exists":
        flash("Name '%s' Is Already Taken, Please Try a Different One!" % name, "error")

    return redirect("/")


@app.route("/logIn", methods=['POST'])
def log_user():
    name = request.form.get("logName")
    passw = request.form.get("logPass")
    
    login = a.log_user_in(name, passw)
    if a.login == "loggedin":
        return redirect("/show_main")
    else:
        flash("ACCOUNT DOES NOT EXISTS - PLEASE TRY A DIFFERENT NAME", "error")
        return redirect("/")
    
@app.route("/show_main")
def show_main():
    
    login = a.login
    name = a.name
    events = a.show_events()

    
    a.login = "loggedin"
    
    return render_template("/in.html", login=login, name=name, events=events)

@app.route("/home", methods=['GET'])
def home():
    name = request.args.get('value')
    
    a.name = name
    
    return redirect("/show_main")


@app.route("/createEvent", methods=['POST'])
def create_event():
    name = request.form.get('name')
    date = request.form.get('date')
    desc = request.form.get('desc')
    user_det = request.form.get('cre_event')
    print(date)
    a.create_ev(name, date, desc, user_det)
    
    return redirect("/show_main")


@app.route("/deleteEvent", methods=['POST'])
def delete_event():
    info = request.form["delete"]

    a.del_event(info)
    
    return redirect("/show_main")
    

@app.route("/logOut", methods=['GET'])
def log_user_out():  
    
    a.log_user_out()
    
    flash("You Have Successfully Logged Out")
    
    return redirect("/")


@app.route("/searchEvent", methods=['GET'])
def search_event():
    word = request.args.get('search')
    user_name = request.args.get('sea_deta')

    a.search(word)
    a.name = user_name

    return redirect("/show_main")
    

@app.route("/edit_event", methods=['POST'])
def edit_event():
    new_name = request.form.get('edName')
    new_date = request.form.get('edDate')
    new_desc = request.form.get('edDesc')
    old_details = request.form.get('ed_event')

    a.edit_event(new_name, new_date, new_desc, old_details)
     
    return redirect("/show_main")


@app.route("/archive_event", methods=['POST'])
def archive_event():
    info = request.form["archive"]
        
    a.arch_eve(info)

    return redirect("/show_main")


@app.route("/show_archive")
def show_archive():
    name = request.args.get('value')
    
    a.show_arch(name)
    
    return redirect("/show_main")


@app.route("/share_with", methods=['POST'])
def share_with():
    share_user = request.form.get('shareName')
    share_details = request.form.get('sha_event')
    
    is_shared = a.share_with(share_user, share_details)
    
    if is_shared == True:
        flash("Your Event has been shared with '%s'" % share_user)
    else:
        flash("Error Sharing, Name '%s' does not exist, please check for spelling mistakes" % share_user)
    
    return redirect("/show_main")
 
 
@app.route("/show_shared_with")
def show_shared_with():
    name = request.args.get('value')
     
    a.show_shared_with(name)
     
    return redirect("/show_main")

    
    
if __name__ == '__main__':
    app.run(debug=True)