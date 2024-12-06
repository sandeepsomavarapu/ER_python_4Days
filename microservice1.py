from flask import Flask,jsonify

app=Flask(__name__)

@app.route('/message',methods=['GET'])
def welcome_micro():
    message={"msg":"welcome to microservice architecture"}
    return jsonify(message)

if __name__=="__main__":
    app.run(port=8000)
