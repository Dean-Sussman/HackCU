import mechanize
from flask import Flask, render_template, request, redirect, url_for

from main import main

app = Flask(__name__)
foodPantries = -1

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
        global foodPantries
        foodPantries = pass_to_backend(street_address, city, state)

        return redirect('./donate_food')
    else:
        return render_template("index.html")


def pass_to_backend(street_address, city, state):
    return main(street_address, city, state);


@app.route('/donate_food')
def donate_food():
    werd = []
    if (foodPantries != -1):
        for var in foodPantries:
            werd.append(var.name)
    return render_template('donate_food.html', list=werd)


if __name__ == '__main__':
    app.run()
