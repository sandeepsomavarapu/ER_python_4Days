from flask import *
app = Flask(__name__)
@app.route("/")
def welcome():
    return "welcome to flask"
@app.route("/index")
def index():
    return "hello !you are in index page"
@app.route("/login/<uname>")
 
def loginapp(uname):
    return "login success Mr :"+uname;
 
@app.route("/register/<int:age>")
def register(age):
    return "Age is %d"%age;
@app.route("/admin")
def admin():
    return "Admin";
@app.route("/employee")
def employee():
    return "Employee";
@app.route("/user/<name>")
def user(name):
    if name=="admin":
        return redirect(url_for('admin'))
    if name=="employee":
        return redirect(url_for('employee'))
 
if __name__=="__main__":
    app.run(debug=True,port=1234)