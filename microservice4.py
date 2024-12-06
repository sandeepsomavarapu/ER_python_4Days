from flask import Flask,jsonify
import requests
app=Flask(__name__)

@app.route("/getemp")
def returnEmp():
    return jsonify({"eid":123,"ename":"sandeep","esal":12000})

if __name__=="__main__":
    app.run(port=8003)
