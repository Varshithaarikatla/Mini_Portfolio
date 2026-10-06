from flask import Flask,render_template
from flask import request,redirect,url_for
app=Flask(__name__)
#@->decorater
@app.route("/")
def func():
    return "<center><h1>welcome to flask app</h1></center>"
@app.route("/greet/<name>")
def greet(name):
    return f"<center style='color: blue;'><h1>hello {name}</h1></center>"
@app.route("/index", methods=['GET', 'POST'])
def myprofile():
    data=None
    if request.method=='POST':
        data=request.form
    return render_template("index.html",data=data)
    

if __name__=="__main__":    
    app.run(debug=True)