from flask import Flask, render_template, request


app = Flask(__name__)

example = {}

example["Question"] = '''Given a string s, find the longest palindromic substring in s.
                        You may assume that the maximum length of s is 1000.'''
example['Example'] = [{'input': '"babad"', 'output': '"bab"', 'note': '"aba" is also a valid answer.'},
                        {'input': '"cbbd"', 'output': '"bb"'}]

@app.route("/", methods= ['GET', 'POST'])
def displayTextEditor():
    code = ''
    result = ''

    if request.method == 'POST':
        code = request.form['code']
        result = runcode(code)
    return render_template("text_editor.html", code=code, result=result, problem=example)

def runcode(code):
    return "Your code result"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
