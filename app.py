from flask import Flask, render_template, redirect, request, jsonify
from events import *
from flask.globals import request
from _ast import Try
from _overlapped import NULL


app = Flask(__name__)



@app.route('/')
def index():
    
    a = Events()
    
    if a.flag == "yes":
        flag = "yes"
    else:
        flag = "no"
    
    events = a.show_events() 
    eveLen = len(events["events"])
    
    return render_template('index.html', events=events, eveLen=eveLen, flag=flag)


@app.route("/createEvent", methods=['GET', 'POST'])
def create_event():
    name = request.args.get('name')
    date = request.args.get('date')
    desc = request.args.get('description')
     
    b = Events()
    create = b.create_ev(name, date, desc)
     
    return redirect("/")
 
 
@app.route("/deleteEvent", methods=['GET', 'POST'])
def delete_event():
    num = request.args.get('num')
     
    c = Events()
    dele = c.del_event(num)
     
    return redirect("/")


@app.route("/deleteEventSearch", methods=['GET', 'POST'])
def delete_event_search():
    num = request.args.get("num")
    
    d = Events()
    dele_sear = d.del_event_sear(num)
    
    return redirect("/")


@app.route("/editEvent", methods=['GET', 'POST'])
def edit_event():
    num = request.args.get('ed_num')
    name = request.args.get('ed_name')
    date = request.args.get('ed_date')
    desc = request.args.get('ed_description')

    e = Events()
    edi = e.edit_event(num, name, date, desc)

    return redirect("/")


@app.route("/searchEvent", methods=['GET', 'POST'])
def search_event():
    searched = request.args.get('sear')

    f = Events()
    sea = f.search_event(searched)

    return redirect("/")



if __name__ == '__main__':
    app.run(debug=True)
    
# set FLASK_APP=app.py
# set FLASK_ENV=development