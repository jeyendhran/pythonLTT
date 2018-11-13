from flask import Flask, request, redirect, url_for

app = Flask(__name__)

@app.route("/hello/<name>")
def hello_user(name):
    return "Hello "+name

@app.route("/hello")
def just_hello():
    return "Hello Guest"

@app.route("/hello/")
def hello_name():
    return "Hello "+request.values.get('name')
    #return "Hello "+request.args.get('name')

@app.route("/data/<int:id>/<int:age>")
def mymethod(id,age):
    return "ID number is "+str(id)+" and age is "+str(age)

@app.route("/user/<user>")
def userlogin(user):
    if user == "jey":
        return redirect(url_for('hello_user',name=user))
    else:
        return redirect(url_for('just_hello'))

@app.route("/login", methods=['POST', 'GET'])
def login():
    print(request.method)
    if request.method == 'POST':
        return "Hello MY name is " + request.form["name"]
    else:
        return "Hello MY name is "+request.values.get("name")

if __name__ == '__main__':
    app.run()
    #app.route(rule,options)