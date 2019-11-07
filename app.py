from flask import Flask, render_template, redirect, request, jsonify
from events import *
from flask.globals import request
from _ast import Try
from _overlapped import NULL


app = Flask(__name__)



@app.route('/')
def index():
    
    a = Events()

    flag = a.flag
    
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


@app.route("/editSeEvent", methods=['GET', 'POST'])
def edit_event_search():
    num = request.args.get('ed_num_sear')
    name = request.args.get('ed_se_na')
    date = request.args.get('ed_se_da')
    desc = request.args.get('ed_se_des')
    
    f = Events()
    edi_sear = f.edit_event_sear(num, name, date, desc)
    
    return redirect("/")
    

@app.route("/searchEvent", methods=['GET', 'POST'])
def search_event():
    searched = request.args.get('sear')

    g = Events()
    sea = g.search_event(searched)

    return redirect("/")


@app.route("/archiveEvent", methods=['GET', 'POST'])
def archive_event():
    num = request.args.get('num')
    
    h = Events()
    arch = h.arch_eve(num)
    
    return redirect("/")


@app.route("/archSeEvent", methods=['GET', 'POST'])
def archive_event_search():
    num = request.args.get('num')
    
    i = Events()
    arch_sea = i.arch_eve_sear(num)

    return redirect("/")


@app.route("/showArchive")
def show_archive():
    
    j = Events()
    show_arch = j.display_arch()
    
    return redirect("/") 


@app.route("/deleteEvArch", methods=['GET', 'POST'])
def delete_event_arch():
    num = request.args.get("num")
    
    k = Events()
    dele_arch = k.del_event_arch(num)
    
    return redirect("/")


@app.route("/shareEvent", methods=['GET', 'POST'])
def share_event():
    num = request.args.get("num")
    
    l = Events()
    share = l.share_eve(num)
    
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)
    
# set FLASK_APP=app.py
# set FLASK_ENV=development