from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def displayTextEditor():
    return render_template("text_editor.html")

@app.route("/process", methods=['GET', 'POST'])
def process():
    code = request.form['code']

    # return code
    return render_template("text_editor.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
