from flask import Flask

# 建立app物件,設定靜態檔案的路徑處理
app = Flask(
    __name__,
    static_folder="static", #靜態檔案的資料夾名稱
    static_url_path="/" #靜態檔案對應網址路徑
)
# 所有在static資料夾底下的檔案,都對應到網址路徑 /abc/檔案名稱

#建立網站首頁的回應方式
@app.route("/") 
def home(): #用來回應路徑"/"的處理函式
    return "Hello Flask" #回傳網站首頁的內容

#建立路徑 /data對應的處理函式
@app.route("/data")
def handledata():
    return "My data"

#動態路由：建立/user/使用者名稱 對應的處理函式
@app.route("/user/<username>")
def handleuser(username):
    if username == "小宇":
        return "你好" +username
    else:
        return "Hello " +username
