from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/<name>")
def greet(name):
    return f"Hello this is {name}"

if __name__ == "__main__":
    app.run(debug=True)