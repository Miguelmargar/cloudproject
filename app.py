from flask import Flask, flash, render_template, redirect, request, jsonify
from events import *


app = Flask(__name__)
app.secret_key = "flashKey"

@app.route('/')
def index():
    
    Events()
    
    return render_template("index.html")

@app.route("/signUp", methods=['POST'])
def sign_user():
    name = request.form.get("signName")
    passw = request.form.get("signPass")
    
    a = Events()
    sign = a.sign_user_up(name, passw)
    
    if sign == "created":
        flash("%s, Your Account Has Been Created" % name.capitalize())
    elif sign == "exists":
        flash("Name '%s' is Already Taken, Please try a different one!" % name)

    return redirect("/")


@app.route("/logIn", methods=['POST'])
def log_user():
    name = request.form.get("logName")
    passw = request.form.get("logPass")
        
    a = Events()
    login = a.log_user_in(name, passw)
    if login == "loggedin":
        return redirect("/show_main")
    else:
        return "ACCOUNT DOES NOT EXISTS - PLEASE TRY A DIFFERENT NAME"
    
@app.route("/show_main")
def show_main():
    
    a = Events()
    events = a.show_events()
    login = Events.login
    name = Events.name
    in_search = Events.sea
    in_arch = Events.arch
    in_share = Events.share
    
    Events.sea = "no"
    Events.arch = "no"
    Events.share = "no"
    
    return render_template("/in.html", login=login, name=name, events=events, in_search=in_search, in_arch=in_arch, in_share=in_share)


@app.route("/createEvent", methods=['POST'])
def create_event():
    name = request.form.get('name')
    date = request.form.get('date')
    desc = request.form.get('desc')

    a = Events()
    a.create_ev(name, date, desc)
    login = Events.login
    user = Events.name
    
    return redirect("/show_main")


@app.route("/deleteEvent", methods=['POST'])
def delete_event():
    event = request.form["delete"]

    a = Events()
    a.del_event(event)
    
    return redirect("/show_main")
    

@app.route("/logOut", methods=['GET'])
def log_user_out():  
    
    a = Events()
    a.log_user_out()
    
    return redirect("/")


@app.route("/searchEvent", methods=['GET'])
def search_event():
    name = request.args.get('search')

    a = Events()
    a.search(name)

    return redirect("/show_main")


@app.route("/get_old_details", methods=['GET', 'POST'])
def get_old_details():
    old_name = request.args.get('old_name')
    old_date = request.args.get('old_date')
    old_desc = request.args.get('old_desc')
    
    a = Events()
    a.get_old_details(old_name, old_date, old_desc)
        
    return redirect("/show_main")
    

@app.route("/edit_event", methods=['POST'])
def edit_event():
    new_name = request.form.get('edName')
    new_date = request.form.get('edDate')
    new_desc = request.form.get('edDesc')
    
    a = Events() 
    a.edit_event(new_name, new_date, new_desc)
     
    return redirect("/show_main")


@app.route("/archive_event", methods=['POST'])
def archive_event():
    event = request.form["archive"]
        
    a = Events()
    a.arch_eve(event)

    return redirect("/show_main")


@app.route("/show_archive")
def show_archive():
    
    a = Events()
    a.show_arch()
    
    return redirect("/show_main")


@app.route("/get_sha_det", methods=['GET'])
def get_share_details():
    sha_name = request.args.get('sha_na')
    sha_date = request.args.get('sha_da')
    sha_desc = request.args.get('sha_desc')

    a = Events()
    a.get_share_details(sha_name, sha_date, sha_desc)
    
    return redirect("/show_main")


@app.route("/share_with", methods=['POST'])
def share_with():
    share_user = request.form.get('shareName')

    a = Events()
    is_shared = a.share_with(share_user)
    
    return redirect("/show_main")
 
 
@app.route("/show_shared_with")
def show_shared_with():
     
    a = Events()
    a.show_shared_with()
     
    return redirect("/show_main")

    
    
    

if __name__ == '__main__':
    app.run(debug=True)