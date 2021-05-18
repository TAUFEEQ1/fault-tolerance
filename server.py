#!/Users/mac/Documents/GitHub/envir4/bin/python
from calcAmount import calcAmount
from flask import Flask,request
from flask_cors import CORS
import sys
import time

app = Flask(__name__)
CORS(app)

global callCount
callCount = 0

@app.route("/calculateAmount",methods=['POST'])
def calculateAmount():
    principal = int(request.form.get("principal"))
    interest = float(request.form.get("interest"))
    tym = int(request.form.get("time"))
    amount = calcAmount(principal,interest,tym)
    global callCount
    callCount = callCount + 1
    if not (callCount % 2):
        time.sleep(5)
    print(amount)
    return str(amount)    


if __name__=="__main__":
    port = 1200 + int(sys.argv[1])
    app.run(host="localhost",port=port)

