from flask import Flask, render_template, request
import logic

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")

@app.route('/sub', methods = ['POST'])
def submit():
    if request.method == "POST" :
        strr = request.form["strings"]
        lis = [strr]
        print(logic.predict_spam(lis))
    return render_template("index.html", n = strr)

if __name__ == '__main__':
    app.run(debug=True)
