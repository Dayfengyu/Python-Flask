from flask import Flask
from flask import request

app = Flask(__name__,static_folder="public",static_url_path="/")


@app.route("/")
def home(): #用來回應路徑"/"的處理函式
    return "您好，歡迎光臨"

app.run() #立刻啟動伺服器