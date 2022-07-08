from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

app.route('/sub', methods = ['POST'])
def submit():
    if request.method == "POST" :
        str = request.form["strings"]
        lis = [str]
        print(logic.predict_spam(lis))
    return render_template("index.html", str = str)

if __name__ == '__main__':
    app.run(debug=True)
