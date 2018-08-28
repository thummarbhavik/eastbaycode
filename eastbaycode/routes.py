from eastbaycode import app
from flask import render_template, request
from eastbaycode.dbi import *

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
        code = request.form['code']
        result = runcode(code)
    return render_template("text_editor.html", code=code, result=result, problem=problem, ex_len=ex_len)

def runcode(code):
    return "Your code result"
