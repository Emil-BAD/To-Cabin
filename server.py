from flask import Flask, url_for, request, render_template
import json

app = Flask(__name__)


@app.route('/training/<prof>')
def index(prof):
    return render_template('base.html', prof=prof)


@app.route('/list_prof/<value>')
def prof_list(value):
    return render_template('prof_list.html', value=value)


if __name__ == '__main__':
    app.run(port=8000, host='127.0.0.1')
