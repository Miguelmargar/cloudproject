from flask import Flask, render_template
from events import *

app = Flask(__name__)

@app.route('/')
def index():
    
    a = Events()
    events = a.show_events()
    
    return render_template('index.html', events=events)


if __name__ == '__main__':
    app.run(debug=True)
    
# set FLASK_APP=app.py
# set FLASK_ENV=development