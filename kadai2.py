import datetime
import calendar

from flask import Flask
app = Flask(__name__)

@app.route("/")

def time():

    a = datetime.datetime.now()
    return a.strftime('%m/%d %H:%M')

if __name__=="__main__":
    app.debug = True
    app.run()