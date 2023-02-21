from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Привет</h1>'


@app.route("/reg")
def register():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.68', port=8080)
