from flask import Flask, render_template, redirect, request, jsonify
from events import *
from flask.globals import request

app = Flask(__name__)

@app.route('/')
def index():
    
    a = Events()
    events = a.show_events()
    eveLen = len(events["events"])
    
    return render_template('index.html', events=events, eveLen=eveLen)


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


if __name__ == '__main__':
    app.run(debug=True)
    
# set FLASK_APP=app.py
# set FLASK_ENV=development