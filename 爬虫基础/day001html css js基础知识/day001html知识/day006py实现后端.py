#wed 前端  后端 

#轻量级wed开发框架
from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/") #配置路由
def index():
    '''返回数据'''
    return render_template("day004form表单.html")
@app.route('/submit')
def submit():
    print (request)

    
if __name__ == '__main__':
    #启动服务器
    app.run()