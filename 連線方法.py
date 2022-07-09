from crypt import methods
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__,static_folder="public",static_url_path="/")

#使用 GET 方法處理路徑 / 的對應函式
@app.route("/")
def home():
    return render_template("index.html")

#用GET處理路徑 /calculate 的對應函式
@app.route("/calculate", methods=["POST"])
def calculate():
    #接收GET方法的 Query String
    #maxNum=int(request.args.get("max",""))
    #接收POST方法的
    maxNum=int(request.form["max"])
    result = 0
    for i in range(1,maxNum+1):
        result += i
    return render_template("result.html" ,data=result)

#處理路徑 /page 的對應函式
@app.route("/page")
def page():
    return render_template("page.html")

#處理路徑 /show 的對應函式
@app.route("/show")
def show():
    name = request.args.get("n","")
    return "歡迎光臨," +name

app.run() #立刻啟動伺服器