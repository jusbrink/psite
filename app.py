#!/usr/bin/python

# Flask
from flask import Flask, render_template, redirect

# APP
app = Flask(__name__)


# LANDING
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/journal/')
def journal():
    return render_template('journal.html')


if __name__ == '__main__':
    # RUN
    app.run(host='0.0.0.0', debug=True)
    #Remember to execute a GET method to initiate the email service.  E.g. Refresh the homepage
