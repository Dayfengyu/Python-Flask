import re
from flask import Flask
from flask import request
from flask import redirect
import json

app = Flask(__name__,static_folder="public",static_url_path="/")

#設定路徑/en/對應的處理函式
@app.route("/en/")
def index_english():
    return json.dumps({
        "status":"ok",
        "text":"Hello Flask" #回傳網站首頁的內容
    })

#設定路徑/zh_TW/對應的處理函式
@app.route("/zh_TW/")
def index_chinese():
    return json.dumps({
        "status":"ok",
        "text":"您好，歡迎光臨"
    },ensure_ascii=False) #指示不要用ascii編碼處理中文

@app.route("/")
def home(): #用來回應路徑"/"的處理函式
    lang = request.headers.get("accept-language")
    if lang.startswith("en"):
        return redirect("/en/") #導向到英文介面
    else:
        return redirect("/zh_TW/") #導向到中文介面

app.run() #立刻啟動伺服器