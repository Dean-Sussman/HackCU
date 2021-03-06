from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    # Displays the index page accessible at '/'
    return render_template('index.html')


@app.route('/donate_food')
def donate_food():
    return render_template('donate_food.html')


if __name__ == '__main__':
    app.run()
