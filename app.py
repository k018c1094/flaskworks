from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/send",methods=["POST"])
def send():
    msg = request.form.get("msg")
    msga = request.form.get("msga")
    return render_template("receive.html", message=msg, messagea=msga)

if __name__=="__main__" :
    app.debug = True
    app.run()
