from flask import Flask
from flask import request
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
    # print("請求方法",request.method)
    # print("通訊協定", request.scheme)
    # print("主機名稱", request.host)
    # print("路徑",request.path)
    # print("完整網址",request.url)
    # print("瀏覽器和作業系統",request.headers.get("user-agent"))
    # print("語言偏好",request.headers.get("accept-language"))
    # print("引薦網址", request.headers.get("referrer"))
    lang = request.headers.get("accept-language")
    print("語言偏好",lang)
    if lang.startswith("en"):
        return "Hello Flask" #回傳網站首頁的內容
    else:
        return "您好，歡迎光臨"

app.run() #立刻啟動伺服器
