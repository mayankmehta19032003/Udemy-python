from flask import Flask,render_template  # Correct import

app = Flask(__name__)  # Use Flask (capital F), not flask (lowercase)

@app.route("/")  
def home():
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)