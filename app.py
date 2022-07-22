from flask import Flask, render_template, request
import logic
import load

app = Flask(__name__)

# Route is the url requested by user
@app.route('/')
def hello_world():  # put application's code here
    k = load.message()
    return render_template("index.html", spam = str(k['spam']), ham = str(k['ham']))


@app.route('/sub', methods=['POST'])
def submit():
    k = load.message()
    if request.method == "POST":
        strr = request.form["strings"]
        lis = [strr]
        prediction = logic.predict_spam(lis)
        print(prediction[0][0])
        return render_template("predict.html", n=prediction, spam = str(k['spam']), ham = str(k['ham']))


if __name__ == '__main__':
    app.run(debug=True)
