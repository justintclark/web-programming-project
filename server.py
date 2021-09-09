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

@route("/greetings")
@route("/greetings/<names>")
def get_name(names="world"):
    names = names.split(',')
    return template("greetings.tpl", name=names)

run(host="localhost", port=8080)