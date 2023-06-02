from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def open_login():
    #打开登录页面
    return render_template("Main.html")

@app.route('/login', methods=["post"])
def login_data():
    #返回登录数据
    return request.form

if __name__ == '__main__':
    app.run()
