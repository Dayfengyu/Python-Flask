from flask import Flask
from flask import request

app = Flask(__name__,static_folder="public",static_url_path="/")

#建立路徑 /getsum對應的處理函式
#利用要求字串提供彈性 : /getSum?min=最小數字&max=最大數字
@app.route("/getSum")
def getSum(): #min+...+max
    #接收要求字串中的參數資料
    minNum = int(request.args.get("min",1))
    maxNum = int(request.args.get("max",100))
    print(minNum)
    print(maxNum)
    result = 0
    for i in range(minNum,maxNum+1):
        result += i  #將結果回應前端
    return "結果："  +str(result)

@app.route("/")
def home(): #用來回應路徑"/"的處理函式
    lang = request.headers.get("accept-language")
    print("語言偏好",lang)
    if lang.startswith("en"):
        return "Hello Flask" #回傳網站首頁的內容
    else:
        return "您好，歡迎光臨"

app.run() #立刻啟動伺服器