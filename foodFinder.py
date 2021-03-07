import mechanize
from flask import Flask, render_template, request, redirect

from main import main

app = Flask(__name__)


@app.route('/')
def index():
    # Displays the index page accessible at '/'
    return render_template('index.html')


@app.route('/address', methods=['GET', 'POST'])
def donate():
    if request.method == "POST":
        street_address = request.form['address']
        city = request.form['city']
        state = request.form['states']
        foodPantries = pass_to_backend(street_address, city, state)
        for var in foodPantries:
            print(var.name, var.url, str(var.foodItems), "\n")
        return redirect('./donate_food')
    else:
        return render_template("index.html")


def pass_to_backend(street_address, city, state):
    return main(street_address, city, state);


@app.route('/donate_food')
def donate_food():
    return render_template('donate_food.html')


if __name__ == '__main__':
    app.run()
