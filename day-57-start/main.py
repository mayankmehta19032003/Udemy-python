from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    random_number = random.randint(1,10)
    current_year = datetime.now().year
    return render_template("index.html",num=random_number, year=current_year)

@app.route('/guess/<name>')
def guess(name):
    response =requests.get(f"https://api.genderize.io/?name={name}")
    response = response.json()
    gender = response['gender']
    return render_template("guess.html",name=name,gender=gender)

@app.route('/blog')
def blog():
    response =requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    all_post = response.json()
    return render_template("blog.html",posts = all_post)

if __name__ == "__main__":
    app.run(debug=True)


