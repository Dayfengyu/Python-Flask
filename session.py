from flask import Flask, render_template, request, session

app = Flask(__name__,static_folder="public",static_url_path="/")

app.secret_key="噓" #設定session的密鑰

@app.route("/")
def home(): #用來回應路徑"/"的處理函式
    return render_template("index.html")

#使用GET方法處理路徑/hello?name=使用者的名字
@app.route("/hello")
def hello():
    name = request.args.get("name","")
    session["username"]=name #session["欄位名稱"]=資料
    return "您好，" +name

#使用GET方法處理路徑/talk
@app.route("/talk")
def talk():
    name = session["username"]
    return name + "很高興見到你"

app.run() #立刻啟動伺服器