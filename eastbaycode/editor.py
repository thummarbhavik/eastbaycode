from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods= ['GET', 'POST'])
def displayTextEditor():
    code = ''
    if request.method == 'POST':
        code = request.form['code']

    return render_template("text_editor.html", code=code)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
