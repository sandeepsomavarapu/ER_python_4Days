from flask import Flask,jsonify
import requests
app=Flask(__name__)

micro2_url="http://127.0.0.1:8001/getrandom"
micro4_url="http://127.0.0.1:8003/getemp"

def call_micro2():
    response=requests.get(micro2_url)
    return response.json().get("rand_no")

@app.route("/getnumber")
def validate_even_odd():
    ranno=call_micro2()
    result="even" if ranno%2==0 else "odd"
    return jsonify({"rand_no":ranno,"evenorodd":result})
@app.route("/employee")
def getEmp():
    response=requests.get(micro4_url)
    print(response)
    return jsonify(response,200)

if __name__=="__main__":
    app.run(port=8002)
