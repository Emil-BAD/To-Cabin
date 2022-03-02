from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/<team>')
def index(team):
    return render_template('cabin.html', team=team.split(', '))


@app.route('/distribution/<team>')
def names_cabin(team):
    return render_template('', team=team)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
