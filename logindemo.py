from flask import *
app = Flask(__name__)

@app.route("/loginuser",methods=['POST'])
def login():
    uname=request.form['uname']
    password=request.form['pass']
    if uname=="ericsson" and password=="india":
        return "Welcome Mr %s"%uname
    
@app.route("/loginuser1",methods=['GET'])
def login1():
    uname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=="ericsson" and password=="india":
        return "Welcome Mr %s"%uname   
     
@app.route("/template")
def message():
    return "<html><body><h1>am from template...</h1></body></html>"

@app.route("/login")
def loginpage():
    return render_template("loginui.html")
@app.route("/message/<msg>")
def msgpage(msg):
    return render_template("message.html",name=msg)      
if __name__=="__main__":
        app.run(debug=True,port=1234)