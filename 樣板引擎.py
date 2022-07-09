import imp
from operator import imod
from flask import Flask
from flask import request
from flask import render_template
app = Flask(__name__,static_folder="public",static_url_path="/")


@app.route("/")
def home(): #用來回應路徑"/"的處理函式
    return render_template("test",name="小宇")

app.run() #立刻啟動伺服器