from eastbaycode import app
from flask import render_template, request
from eastbaycode.dbi import *
from eastbaycode.runner import *
from eastbaycode.msgqueue import *

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
        msg_sent = {"code": code, "inputs": inputs,"prototype": "def sayHello(s)","handle": 38}
        msg = '{}'.format(msg_sent)
        push_msg(qname="msgQueue", msg=msg)
        result = get_result(qname="msgQueue")

    return render_template("text_editor.html", code=code, result=result, problem=problem, ex_len=ex_len)
