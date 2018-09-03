from eastbaycode import app
from flask import render_template, request
from eastbaycode.dbi import *
from eastbaycode.runner import *

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
        result = runcode(code, inputs)
    return render_template("text_editor.html", code=code, result=result, problem=problem, ex_len=ex_len)
