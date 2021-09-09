from bottle import route, run, template

#http://localhost:8080 <route>

@route("/")
def get_index():
    return ("Hello!")
    

@route("/hello")
def get_index():
    return ("Hello!")

@route("/hello/<name>")
def get_name(name="world"):
    return template("hello.tpl", name="Bob", extra="Happy birthday!")

@route("/greet")
@route("/greet/<name>")
def get_name(name="world"):
    return template("hello.tpl", name="Bob", extra=None)

@route("/greeting/<names>")
def get_greeting(names):
    names = names.split(',')
    return template("greetings", names=names)

run(host="localhost", port=8080)