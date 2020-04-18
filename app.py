from flask import Flask, flash, render_template, redirect, request, url_for, session, g
from events import *


app = Flask(__name__)
app.secret_key = flash_key

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
    
    state = a.log_user_in(name, passw)
    pic = a.check_pic(name)
    print(pic)
    if state == "loggedin":
        session["user"] = name
        session["state"] = state
        
        if pic != 'no':
            session['pic_name'] = pic
        
        return redirect("/show_main")
    
    elif state == "nameerr":
        flash("ACCOUNT DOES NOT EXISTS - PLEASE TRY A DIFFERENT NAME", "error")
        
        return redirect("/")
    
    elif state == "passerr":
        flash("WRONG PASSWORD - PLEASE TRY CHECKING YOUR PASSWORD", "error")
        
        return redirect("/")
 
@app.before_request
def before_request():
    g.user = None
    if "user" in session:
        g.user = session["user"]
    
@app.route("/show_main", methods=['GET', 'POST'])
def show_main():
    
    if g.user:
        if request.method == 'POST':
            word = request.form.get('search')
            session["state"] = "loginsea"       
            events = a.show_events(session["user"], session["state"], word)
        else:
            events = a.show_events(session["user"], session["state"])
        
        return render_template("/in.html", events=events)
    else:
        flash("ERROR, Something Went Wrong, Please Try Logging In Again", "error")
        return redirect("/")

@app.route("/home")
def home():
    session["state"] = "loggedin"
    return redirect("/show_main")


@app.route("/createEvent", methods=['POST'])
def create_event():
    nameForm = request.form.get('name')
    date = request.form.get('date')
    time = request.form.get('time')
    desc = request.form.get('desc')

    user_det = a.create_ev(nameForm, date, time, desc, session["user"])
    
    return redirect("/show_main")


@app.route("/deleteEvent", methods=['POST'])
def delete_event():
    info = request.form["delete"]

    user_dets = a.del_event(info)
    
    flash("Task Deleted Successfully!", "good")
    
    return redirect("/show_main")
    

@app.route("/logOut", methods=['GET'])
def log_user_out():  
    session.pop("user", None)
    session.pop("state", None)
    session.pop("pic_name", None)
    flash("You Have Successfully Logged Out", "good")
    
    return redirect("/")
    

@app.route("/edit_event", methods=['POST'])
def edit_event():
    new_name = request.form.get('edName')
    new_date = request.form.get('edDate')
    new_time = request.form.get('edTime')
    new_desc = request.form.get('edDesc')
    old_details = request.form.get('ed_event')
    
    user_dets = a.edit_event(new_name, new_date, new_time, new_desc, old_details)
     
    return redirect("/show_main")


@app.route("/archive_event", methods=['POST'])
def archive_event():
    info = request.form["archive"]
        
    name = a.arch_eve(info)
    
    flash("Task Successfully Archived!", "good")

    return redirect("/show_main")


@app.route("/show_archive")
def show_archive():
    session["state"] = "loginarch"
    return redirect("/show_main")


@app.route("/share_with", methods=['POST'])
def share_with():
    share_user = request.form.get('shareName')
    share_details = request.form.get('sha_event')
    
    is_shared = a.share_with(share_user, share_details)
    
    if is_shared == "True":
        flash("Your Event has been shared with '%s'" % share_user, "good")
    else:
        flash("Error Sharing, Name '%s' does not exist, please check for spelling mistakes" % share_user, "error")
    
    return redirect("/show_main")
 
 
@app.route("/show_shared_with")
def show_shared_with():
    session["state"] = "loginsha"
    return redirect("/show_main")


@app.route("/change_img", methods=['POST'])
def change_img():
    user_photo = request.files['myFile']
    user = session["user"]
    
    picture_changed = a.change_user_pic(user_photo, user)
    
    session['pic_name'] = picture_changed
    print(session['pic_name'])
    return redirect("/show_main")
    
    
    
if __name__ == '__main__':
    app.run(debug=True)