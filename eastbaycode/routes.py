import json
from flask import render_template, request
from eastbaycode import app
from eastbaycode.dbi import connection, getProblems, getTestCase
from eastbaycode.runner import *
from eastbaycode.msgqueue import push_msg, get_result

@app.route("/index")
def hello():
    return "Welcome to EASTBAY CODE!"

@app.route("/", methods= ['GET', 'POST'])
def displayTextEditor():
    code = ''
    result = ''
    problem = getProblems(1)
    ex_len = len(problem['example'])
    if request.method == 'POST':
        inputs = getTestCase(1)
        code = request.form['code']
        # result = runcode(code, inputs) - just for subprocess.run
        # push msg to redis queue
        msg = json.dumps({"code": code, "inputs": inputs,"prototype": "def sayHello(s)","handle": 38})
        push_msg(qname="msgQueue", msg=msg)
        result = get_result(qname="msgQueue")

    return render_template("text_editor.html", code=code, result=result, problem=problem, ex_len=ex_len)
