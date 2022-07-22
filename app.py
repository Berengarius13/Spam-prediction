from flask import Flask, render_template, request
import logic

app = Flask(__name__)

# Route is the url requested by user
@app.route('/')
def hello_world():  # put application's code here
    return render_template("index.html")


@app.route('/sub', methods=['POST'])
def submit():
    if request.method == "POST":
        strr = request.form["strings"]
        lis = [strr]
        prediction = logic.predict_spam(lis)
        print(prediction[0])
        return render_template("index.html", n=prediction)


if __name__ == '__main__':
    app.run(debug=True)
