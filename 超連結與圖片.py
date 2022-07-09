from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__,static_folder="public",static_url_path="/")

#處理路徑 / 的對應函式
@app.route("/")
def home():
    return render_template("index.html")

#處理路徑 /page 的對應函式
@app.route("/page")
def page():
    return render_template("page.html")

app.run() #立刻啟動伺服器