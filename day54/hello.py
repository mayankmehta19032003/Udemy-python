from flask import Flask

app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"


# @app.route("/<name>")
# def greet(name):
#     return f"Hello this is {name}"
def make_bold(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def make_em(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper


@app.route("/bye")
@make_bold
@make_em
def bye():
    return "Bye!"



# if __name__ == "__main__":
#     app.run(debug=True)