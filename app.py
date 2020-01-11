from flask import Flask, flash, render_template, redirect, request, url_for
from events import *
from threading import Lock

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
    
    login = a.log_user_in(name, passw)
    
    if a.login == "loggedin":
        return redirect(url_for("show_main", name=name))
    elif a.login == "nameerr":
        flash("ACCOUNT DOES NOT EXISTS - PLEASE TRY A DIFFERENT NAME", "error")
        return redirect("/")
    elif a.login == "passerr":
        flash("WRONG PASSWORD - PLEASE TRY CHECKING YOUR PASSWORD", "error")
        return redirect("/")
    
@app.route("/show_main")
def show_main():
    login = a.login
    name = request.args.get('name')

    events = a.show_events(name)
    
    a.login = ""
    a.name = ""
    return render_template("/in.html", login=login, name=name, events=events)

@app.route("/home", methods=['GET'])
def home():
    details = request.args.get('value')
    
    pat = r"'(.*?)'"
    details = re.findall(pat, details)
    
    name = details[0]
    a.login = details[1]
    
    return redirect(url_for("show_main", name=name))


@app.route("/createEvent", methods=['POST'])
def create_event():
    nameForm = request.form.get('name')
    date = request.form.get('date')
    time = request.form.get('time')
    desc = request.form.get('desc')
    user_det = request.form.get('cre_event')

    user_det = a.create_ev(nameForm, date, time, desc, user_det)
    
    name = user_det[0]
    login = user_det[1] #need to pass it to show_main
    
    return redirect(url_for("show_main", name=name))


@app.route("/deleteEvent", methods=['POST'])
def delete_event():
    info = request.form["delete"]

    user_dets = a.del_event(info)
    
    name = user_dets[0]
    login = user_dets[1]
    
    flash("Task Deleted Successfully!", "good")
    
    return redirect(url_for("show_main", name=name))
    

@app.route("/logOut", methods=['GET'])
def log_user_out():  
    
    flash("You Have Successfully Logged Out", "good")
    
    return redirect("/")


@app.route("/searchEvent", methods=['POST'])
def search_event():
    word = request.form.get('search')
    user_name = request.form.get('sea_deta')

    a.search(word)
    name = user_name

    return redirect(url_for("show_main", name=name))
    

@app.route("/edit_event", methods=['POST'])
def edit_event():
    new_name = request.form.get('edName')
    new_date = request.form.get('edDate')
    new_time = request.form.get('edTime')
    new_desc = request.form.get('edDesc')
    old_details = request.form.get('ed_event')
    
    user_dets = a.edit_event(new_name, new_date, new_time, new_desc, old_details)
    
    name = user_dets[0]
     
    return redirect(url_for("show_main", name=name))


@app.route("/archive_event", methods=['POST'])
def archive_event():
    info = request.form["archive"]
        
    name = a.arch_eve(info)
    
    flash("Task Successfully Archived!", "good")

    return redirect(url_for("show_main", name=name))


@app.route("/show_archive")
def show_archive():
    name = request.args.get('value')
    
    a.login = "loginarch"
    name = name.replace("'", "")
    
    return redirect(url_for("show_main", name=name))


@app.route("/share_with", methods=['POST'])
def share_with():
    share_user = request.form.get('shareName')
    share_details = request.form.get('sha_event')
    
    is_shared = a.share_with(share_user, share_details)
    
    if is_shared[0] == "True":
        flash("Your Event has been shared with '%s'" % share_user, "good")
    else:
        flash("Error Sharing, Name '%s' does not exist, please check for spelling mistakes" % share_user, "error")
    
    name = is_shared[1]
    
    return redirect(url_for("show_main", name=name))
 
 
@app.route("/show_shared_with")
def show_shared_with():
    name = request.args.get('value')
     
    a.login = "loginsha"
    name = name.replace("'", "")
     
    return redirect(url_for("show_main", name=name))

    
    
if __name__ == '__main__':
    app.run(debug=True)