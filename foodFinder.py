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
    value = ""
    if (foodPantries != -1):
        for var in foodPantries:
            print(var.foodItems)
            if len(var.foodItems) > 2:
                var.foodItems = var.foodItems.replace("[", "").replace("]", "").replace("'", "").split(", ")
            else:
                var.foodItems = []
            value+=(makeTable(var.name, var.url, var.foodItems))
    return render_template('donate_food.html', value=value)

def makeTable(name, url, foodItems):
    headers = """
        <h2>{}</h2>
        <h3><a href="{}">website</a></h3>""".format(name, url)
    if len(foodItems) < 1:
        return headers + "</br>"
    list = """<h3>Items Needed</h3>
        <ul> 
            {0}
        </ul> """

    li = "<li>{0}</li>"
    items = []

    for food in foodItems:
        items.append(li.format(food))
    html = headers + list
    return html.format("".join(items))+ "</br>"


if __name__ == '__main__':
    app.run()
