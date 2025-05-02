from flask import Flask  # Correct import

app = Flask(__name__)  # Use Flask (capital F), not flask (lowercase)

@app.route("/")  
def hello():
    return "hello"  
