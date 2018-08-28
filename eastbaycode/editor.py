from flask import Flask, render_template, request
import MySQLdb
from config import Config

app = Flask(__name__)
config = Config()

# Config MySQL
def connection():
    conn = MySQLdb.connect(host=config.dbhost,
                           user=config.dbuser,
                           passwd=config.dbpw)
    # save data output to dictionary
    cur = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    return cur, conn

def getProblems(id):
    problem = {}
    cur, conn = connection()
    query1 = '''SELECT title, content from eastbaycode.problems where id={}'''.format(id)
    query2 = '''SELECT input, output from eastbaycode.examples where problem_id={}'''.format(id)
    cur.execute(query1)
    question = cur.fetchone()
    problem['Title'] = question['title']
    problem['Question'] = question['content']
    cur.execute(query2)
    examples = cur.fetchall()
    problem['Example'] = examples
    conn.close()
    return problem

@app.route("/", methods= ['GET', 'POST'])
def displayTextEditor():
    code = ''
    result = ''
    problem = getProblems(1)
    if request.method == 'POST':
        code = request.form['code']
        result = runcode(code)
    return render_template("text_editor.html", code=code, result=result, problem=problem)

def runcode(code):
    return "Your code result"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
