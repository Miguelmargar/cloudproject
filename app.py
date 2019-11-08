from flask import Flask, render_template, redirect, request, jsonify
from events import *
from flask.globals import request
from _ast import Try
from _overlapped import NULL
from encodings import undefined
from enum import Flag


app = Flask(__name__)



@app.route('/')
def index():
    global a
    a = Events()
    logged = "no"
    events = []

    try:
        if len(det) == 2:
            logged = "yes"
        else:
            logged = "no"
        
        events = a.show_events(det[0], det[1])
    except:
        pass    
    eveLen = len(events) 
    
    try:
        if total_flag == "no":
            flag = "no"
        if total_flag == "search":
            flag = "search"
        if total_flag == "archive":
            flag = "archive"
    except:
        flag = "no"

    return render_template('index.html', logged=logged, eveLen=eveLen, events=events, flag=flag)


@app.route("/signUp", methods=['GET', 'POST'])
def sign_user():
    name = request.args.get('name')
    passw = request.args.get('pass')
    
    signup = a.sign_user_up(name, passw)

    return jsonify(signup)


@app.route("/logIn", methods=['GET', 'POST'])
def log_user():
    name = request.args.get('namelog')
    passw = request.args.get('passlog') 

    login = a.log_user_in(name, passw)

    return jsonify(login)

@app.route("/loggedMain", methods=['GET', 'POST'])
def show_main():
    global name_in
    global passw_in

    name_in = request.args.get('namelog')
    passw_in = request.args.get('passlog')

    global det
    det = [name_in, passw_in]
    return redirect("/")


@app.route("/logout", methods=['GET', 'POST'])
def log_user_out():
    
    out = a.log_user_out(name_in, passw_in)
    global det
    det = ""
    
    return redirect("/")


@app.route("/createEvent", methods=['GET', 'POST'])
def create_event():
    name = request.args.get('name')
    date = request.args.get('date')
    desc = request.args.get('description')
    
    file_name = name_in + passw_in + ".json"
    
    a = Events()
    create = a.create_ev(name, date, desc, file_name)
     
    return redirect("/")
 
 
@app.route("/deleteEvent", methods=['GET', 'POST'])
def delete_event():
    num = request.args.get('num')
     
    file_name = name_in + passw_in + ".json" 
    
    c = Events()
    dele = c.del_event(num, file_name)
     
    return redirect("/")


@app.route("/deleteEventSearch", methods=['GET', 'POST'])
def delete_event_search():
    num = request.args.get("num")
    
    file_name = name_in + passw_in + ".json"
    
    d = Events()
    dele_sear = d.del_event_sear(num, file_name)
    
    return redirect("/")


@app.route("/editEvent", methods=['GET', 'POST'])
def edit_event():
    num = request.args.get('ed_num')
    name = request.args.get('ed_name')
    date = request.args.get('ed_date')
    desc = request.args.get('ed_description')

    file_name = name_in + passw_in + ".json"

    e = Events()
    edi = e.edit_event(num, name, date, desc, file_name)

    return redirect("/")


@app.route("/editSeEvent", methods=['GET', 'POST'])
def edit_event_search():
    num = request.args.get('ed_num_sear')
    name = request.args.get('ed_se_na')
    date = request.args.get('ed_se_da')
    desc = request.args.get('ed_se_des')
    
    file_name = name_in + passw_in + ".json"
    
    f = Events()
    edi_sear = f.edit_event_sear(num, name, date, desc, file_name)
    
    return redirect("/")
    

@app.route("/searchEvent", methods=['GET', 'POST'])
def search_event():
    searched = request.args.get('sear')

    file_name = name_in + passw_in + ".json"

    g = Events()
    sea = g.search_event(searched, file_name)
    
    global total_flag
    total_flag = g.flag
    
    return redirect("/")


@app.route("/archiveEvent", methods=['GET', 'POST'])
def archive_event():
    num = request.args.get('num')
    
    file_name = name_in + passw_in + ".json"
    
    h = Events()
    arch = h.arch_eve(num, file_name)
    
    return redirect("/")


@app.route("/archSeEvent", methods=['GET', 'POST'])
def archive_event_search():
    num = request.args.get('num')
    
    file_name = name_in + passw_in + ".json"
    
    i = Events()
    arch_sea = i.arch_eve_sear(num, file_name)

    return redirect("/")


@app.route("/showArchive")
def show_archive():
    
    j = Events()
    show_arch = j.display_arch()
    
    global total_flag
    total_flag = j.flag
    
    return redirect("/") 


@app.route("/deleteEvArch", methods=['GET', 'POST'])
def delete_event_arch():
    num = request.args.get("num")
    
    file_name = name_in + passw_in + ".json"
    
    k = Events()
    dele_arch = k.del_event_arch(num, file_name)
    
    
    
    return redirect("/")


@app.route("/shareEvent", methods=['GET', 'POST'])
def share_event():
    num = request.args.get("num")
    
    file_name = name_in + passw_in + ".json"
    
    l = Events()
    share = l.share_eve(num)
    
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
    
# set FLASK_APP=app.py
# set FLASK_ENV=development