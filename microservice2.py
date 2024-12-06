from flask import Flask,jsonify
import random
app=Flask(__name__)

@app.route("/getrandom")
def random_number():
    random_no=random.randint(1,1000)
    return jsonify({"rand_no":random_no})

if __name__=="__main__":
    app.run(port=8001)
